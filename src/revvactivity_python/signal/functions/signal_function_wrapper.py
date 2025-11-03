from typing import Any

from revvactivity_python.signal.functions.signal_function import SignalFunction
from revvactivity_python.signal.listeners.signal_update_listener import SignalUpdateListener
from revvactivity_python.signal.signals.signal import Signal


class SignalFunctionWrapper:
    def on_update_signals(self, signal_function: SignalFunction, update_listener: SignalUpdateListener[Any]) -> None:
        signals = self.__get_signals(signal_function)
        for signal in signals.values():
            signal.on_update(update_listener)
    
    def __get_signals(self, signal_function: SignalFunction) -> dict[str, Signal[Any]]:
        return {
            name: signal_function.__globals__[name]
            for name in signal_function.__code__.co_names
            if name in signal_function.__globals__
        }