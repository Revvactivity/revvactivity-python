from unittest.mock import call, Mock

from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal
from tests.revvactivity_python.signal.signals.signal import SignalTest


class WriteSignalTest(SignalTest):
    def _get_signal(self, value: str) -> Signal[str]:
        return WriteSignal(value)
    
    def test_set_value(self) -> None:
        self.set_value(lambda s, v: s.set_value(v))
    
    def test_update_value(self) -> None:
        write_signal = WriteSignal()

        self.assertEqual(write_signal.get_value(), None)

        first_value = "Hello"

        write_signal.update_value(lambda v: first_value)

        self.assertEqual(write_signal.get_value(), first_value)

        appendix = ", World!"

        write_signal.update_value(lambda v: v + appendix)

        self.assertEqual(write_signal.get_value(), first_value + appendix)
    
    def test_change_value(self) -> None:
        write_signal = WriteSignal()

        change_listener = Mock()

        self.assertEqual(write_signal.get_value(), None)

        write_signal.on_change(change_listener)

        first_value = "Hello"

        first_call = call(None, first_value)

        write_signal.change_value(lambda v: first_value)

        self.assertEqual(write_signal.get_value(), first_value)
        
        change_listener.assert_has_calls([first_call])

        write_signal.change_value(lambda v: v)

        self.assertEqual(write_signal.get_value(), first_value)
        
        change_listener.assert_has_calls([first_call])

        appendix = ", World!"

        second_call = call(first_value, first_value + appendix)

        write_signal.change_value(lambda v: v + appendix)

        self.assertEqual(write_signal.get_value(), first_value + appendix)
        
        change_listener.assert_has_calls([first_call, second_call])
