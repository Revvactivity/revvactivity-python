from typing import TypeVar

from revvactivity_python.javascript.javascript_framework import JavaScriptFramework
from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal


T = TypeVar("T")

class React(JavaScriptFramework):
    def __init__(self):
        super().__init__()

    @staticmethod
    def use_state(value: T) -> WriteSignal[T]:
        return JavaScriptFramework._state(value)
    
    @staticmethod
    def use_memo(derived: SignalDerived[T]) -> Signal[T]:
        return JavaScriptFramework._derived(derived)
    
    @staticmethod
    def use_effect(effect: SignalEffect) -> None:
        JavaScriptFramework._effect(effect)