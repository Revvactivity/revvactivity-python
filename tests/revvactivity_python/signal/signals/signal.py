import unittest
from unittest.mock import Mock
from typing import Callable

from revvactivity_python.signal.signals.signal import Signal


class SignalTest(unittest.TestCase):
    def setUp(self):
        self._first_value = "Foo"
        self._second_value = "Bar"
        self._third_value = "Baz"

        self._first_signal = self._get_signal(self._first_value)
        self._second_signal = self._get_signal(self._second_value)

        self._update_listener = Mock()
        self._change_listener = Mock()

    def _get_signal(self, value: str) -> Signal[str]:
        return Signal(value)

    def test_eq_true(self) -> None:
        signal_1 = self._get_signal(self._first_value)
        signal_2 = self._get_signal(self._first_value)

        self.assertEqual(signal_1, signal_2)

    def test_eq_false(self) -> None:
        signal_1 = self._get_signal(self._first_value)
        signal_2 = self._get_signal(self._second_value)

        self.assertNotEqual(signal_1, signal_2)

    def test_eq_false_no_signal(self) -> None:
        signal_1 = self._get_signal(self._first_value)
        signal_2 = {}

        self.assertNotEqual(signal_1, signal_2)

    def test_call(self) -> None:
        self.assertEqual(self._first_signal(), self._first_value)
    
    def test_get_value(self) -> None:
        self.assertEqual(self._first_signal.get_value(), self._first_value)

    def test__set_value(self) -> None:
        self.set_value(lambda s, v: s._set_value(v))

    def set_value(self, method: Callable[[Signal, str], None]) -> None:
        for value in [self._first_value, self._second_value]:
            self.setUp()
            with self.subTest(value=value):
                self.assertEqual(self._first_signal.get_value(), self._first_value)

                self._first_signal.on_update(self._update_listener)
                self._first_signal.on_change(self._change_listener)

                method(self._first_signal, value)

                self.assertEqual(self._first_signal.get_value(), value)

                self._update_listener.assert_called_once_with(self._first_value, value)
                if self._first_value != value:
                    self._change_listener.assert_called_once_with(self._first_value, value)

    def test__notify_update_listeners(self) -> None:
        self.update_listeners()

    def test__notify_change_listeners(self) -> None:
        self.change_listeners()

    def test_on_update(self) -> None:
        self.update_listeners()

    def test_on_change(self) -> None:
        self.change_listeners()

    def update_listeners(self) -> None:
        self._first_signal.on_update(self._update_listener)

        self._first_signal._notify_update_listeners(self._second_value)
        
        self._update_listener.assert_called_once_with(self._second_value, self._first_value)

    def change_listeners(self) -> None:
        self._first_signal.on_change(self._change_listener)

        self._first_signal._notify_change_listeners(self._second_value)
        
        self._change_listener.assert_called_once_with(self._second_value, self._first_value)

    def test_bind_value_from(self) -> None:
        self.binding_test(
            self._first_signal,
            self._second_signal,
            self._first_value,
            self._second_value,
            lambda: self._first_signal.bind_value_from(self._second_signal)
        )

    def test_bind_value_to(self) -> None:
        self.binding_test(
            self._second_signal,
            self._first_signal,
            self._second_value,
            self._first_value,
            lambda: self._first_signal.bind_value_to(self._second_signal)
        )

    def binding_test(self,
                     signal_one: Signal[str],
                     signal_two: Signal[str],
                     value_one: str,
                     value_two: str,
                     binder: Callable[[], None]) -> None:
        self.assertEqual(signal_one(), value_one)

        binder()
        
        self.assertEqual(signal_one(), value_two)

        value_three = self._third_value

        signal_two._set_value(value_three)
        
        self.assertEqual(signal_one(), value_three)