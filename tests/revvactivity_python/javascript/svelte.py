from typing import Callable, Type, TypeVar

from revvactivity_python.javascript.javascript_framework import JavaScriptFramework
from revvactivity_python.javascript.svelte import Svelte
from revvactivity_python.signal.functions.signal_derived import SignalDerived
from revvactivity_python.signal.functions.signal_effect import SignalEffect
from revvactivity_python.signal.signals.signal import Signal
from revvactivity_python.signal.signals.write_signal import WriteSignal
from tests.revvactivity_python.javascript.javascript_framework import JavaScriptFrameworkTest


T = TypeVar("T")

class SvelteTest(JavaScriptFrameworkTest):
    def _get_type(self) -> Type[JavaScriptFramework]:
        return Svelte

    def _get_state_function(self) -> Callable[[T], WriteSignal[T]]:
        return Svelte.state

    def _get_derived_function(self) -> Callable[[SignalDerived[T]], Signal[T]]:
        return Svelte.derived

    def _get_effect_function(self) -> Callable[[SignalEffect], None]:
        return Svelte.effect