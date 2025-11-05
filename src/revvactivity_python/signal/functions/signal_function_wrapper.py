from typing import Any

from revvactivity_python.signal.functions.signal_function import SignalFunction
from revvactivity_python.signal.listeners.signal_update_listener import SignalUpdateListener
from revvactivity_python.signal.signals.signal import Signal


class SignalFunctionWrapper:
    def on_update_signals(self, signal_function: SignalFunction, update_listener: SignalUpdateListener[Any]) -> None:
        signals = self.__get_signals(signal_function)
        for signal in signals:
            signal.on_update(update_listener)
    
    def __get_signals(self, signal_function: SignalFunction) -> list[Signal[Any]]:
        globals = [
            signal_function.__globals__[name]
            for name in signal_function.__code__.co_names
            if name in signal_function.__globals__
        ]
        closures = [cell.cell_contents for cell in signal_function.__closure__] if signal_function.__closure__ else []
        all_vars = globals + closures
        return [item for item in all_vars if isinstance(item, Signal)]