import unittest
from unittest.mock import call, Mock

from revvactivity_python.signal.functions.signal_function_wrapper import SignalFunctionWrapper
from revvactivity_python.signal.signals.write_signal import WriteSignal


class SignalFunctionWrapperTest(unittest.TestCase):
    def setUp(self):
        self._signal_1 = WriteSignal()
        self._signal_2 = WriteSignal()
        self._update_listener = Mock()

        self._signal_function = lambda: self._signal_1() + "" + self._signal_2()

        self._signal_function_wrapper = SignalFunctionWrapper()
    
    def test_on_update_signals(self) -> None:
        self._signal_function_wrapper.on_update_signals(self._signal_function, self._update_listener)

        signal_1_value = "Foo"
        self._signal_1.set_value(signal_1_value)

        signal_2_value = "Bar"
        self._signal_2.set_value(signal_2_value)
        
        self._update_listener.assert_has_calls(
            [
                call(None, signal_1_value),
                call(None, signal_2_value),
            ],
            any_order=False,
        )
        self.assertEqual(self._update_listener.call_count, 2)