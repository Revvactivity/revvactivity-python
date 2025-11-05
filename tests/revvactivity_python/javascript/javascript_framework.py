import unittest
from typing import Callable, Type, TypeVar

from revvactivity_python.javascript.javascript_framework import JavaScriptFramework
from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal


T = TypeVar("T")

class Counter:
    def __init__(self, value: int):
        self.value = value

    def __call__(self) -> int:
        return self.value
    
    def increment(self) -> None:
        self.value += 1

class JavaScriptFrameworkTest(unittest.TestCase):
    def _get_type(self) -> Type[JavaScriptFramework]:
        return JavaScriptFramework

    def _get_state_function(self) -> Callable[[T], WriteSignal[T]]:
        return JavaScriptFramework._state

    def _get_derived_function(self) -> Callable[[SignalDerived[T]], Signal[T]]:
        return JavaScriptFramework._derived

    def _get_effect_function(self) -> Callable[[SignalEffect], None]:
        return JavaScriptFramework._effect

    def test_constructor(self) -> None:
        with self.assertRaises(RuntimeError):
            type = self._get_type()
            type()

    def test__state(self) -> None:
        value = "Hello, World!"

        expected = WriteSignal(value)

        state = self._get_state_function()
        actual = state(value)

        self.assertEqual(actual, expected)
    
    def test__derived(self) -> None:
        factor_1 = 10
        factor_2 = 20

        write_signal = WriteSignal(factor_2)

        derived = self._get_derived_function()
        derived_signal = derived(lambda: write_signal.get_value() * factor_1)

        self.assertEqual(derived_signal.get_value(), factor_2 * factor_1)

        factor_2 = 30
        write_signal.set_value(factor_2)

        self.assertEqual(derived_signal.get_value(), factor_2 * factor_1)

        factor_2 = 40
        write_signal.set_value(factor_2)

        self.assertEqual(derived_signal.get_value(), factor_2 * factor_1)
    
    def test__effect(self) -> None:
        counter = 0
        atomic_counter = Counter(counter)
        write_signal = WriteSignal()

        self.assertEqual(atomic_counter(), counter)

        effect = self._get_effect_function()
        def get_and_increment():
            write_signal.get_value()
            atomic_counter.increment()
        effect(get_and_increment)

        counter += 1
        self.assertEqual(atomic_counter(), counter)

        write_signal.set_value("Foo")
        counter += 1
        self.assertEqual(atomic_counter(), counter)

        write_signal.set_value("Bar")
        counter += 1
        self.assertEqual(atomic_counter(), counter)