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