from typing import TypeVar

from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.functions.signal_function_wrapper import SignalFunctionWrapper
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal


T = TypeVar("T")

class JavaScriptFramework:
    def __init__(self):
        raise RuntimeError()

    @staticmethod
    def _state(value: T) -> WriteSignal[T]:
        return WriteSignal(value)
    
    @staticmethod
    def _derived(derived: SignalDerived[T]) -> Signal[T]:
        write_signal = WriteSignal(derived())
        SignalFunctionWrapper().on_update_signals(derived, lambda v: write_signal.set_value(derived()))

        signal = Signal(derived())
        signal.bind_value_from(write_signal)
        return signal
    
    @staticmethod
    def _effect(effect: SignalEffect) -> None:
        SignalFunctionWrapper().on_update_signals(effect, lambda v: effect())
        effect()