from typing import TypeVar

from revvactivity_python.javascript.javascript_framework import JavaScriptFramework
from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal


T = TypeVar("T")

class Vue(JavaScriptFramework):
    def __init__(self):
        super().__init__()

    @staticmethod
    def ref(value: T) -> WriteSignal[T]:
        return JavaScriptFramework._state(value)
    
    @staticmethod
    def computed(derived: SignalDerived[T]) -> Signal[T]:
        return JavaScriptFramework._derived(derived)
    
    @staticmethod
    def watch_effect(effect: SignalEffect) -> None:
        JavaScriptFramework._effect(effect)