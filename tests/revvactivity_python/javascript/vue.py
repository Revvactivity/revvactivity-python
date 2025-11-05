from typing import Callable, Type, TypeVar

from revvactivity_python.javascript.javascript_framework import JavaScriptFramework
from revvactivity_python.javascript.vue import Vue
from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal
from tests.revvactivity_python.javascript.javascript_framework import JavaScriptFrameworkTest


T = TypeVar("T")

class VueTest(JavaScriptFrameworkTest):
    def _get_type(self) -> Type[JavaScriptFramework]:
        return Vue

    def _get_state_function(self) -> Callable[[T], WriteSignal[T]]:
        return Vue.ref

    def _get_derived_function(self) -> Callable[[SignalDerived[T]], Signal[T]]:
        return Vue.computed

    def _get_effect_function(self) -> Callable[[SignalEffect], None]:
        return Vue.watch_effect