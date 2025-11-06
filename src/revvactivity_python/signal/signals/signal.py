from inspect import signature
from typing import Generic, TypeVar

from revvactivity_python.signal.listeners.signal_change_listener import SignalChangeListener
from revvactivity_python.signal.listeners.signal_update_listener import SignalUpdateListener


T = TypeVar("T")
T_extends = TypeVar("T_extends")
T_super = TypeVar("T_super")

class Signal(Generic[T]):
    def __init__(self, value: T | None = None):
        super().__init__()
        self.__value: T | None = value
        self.__update_listeners: list[SignalChangeListener[T_super]] = []
        self.__change_listeners: list[SignalChangeListener[T_super]] = []

    def __eq__(self, other):
        if not isinstance(other, Signal):
            return False
        return self.__value == other.__value
    
    def __call__(self) -> T | None:
        return self.get_value()

    def get_value(self) -> T | None:
        return self.__value
    
    def _set_value(self, value: T | None) -> None:
        old_value = self.__value
        self.__value = value

        self._notify_update_listeners(old_value)
        if old_value != value:
            self._notify_change_listeners(old_value)

    def _notify_update_listeners(self, old_value: T | None) -> None:
        for update_listener in self.__update_listeners:
            update_listener(old_value, self.__value)

    def _notify_change_listeners(self, old_value: T | None) -> None:
        for change_listener in self.__change_listeners:
            change_listener(old_value, self.__value)
    
    def on_update(self, listener: SignalUpdateListener[T_super] | SignalChangeListener[T_super]) -> None:
        self.__on_helper(listener, self.__update_listeners)
    
    def on_change(self, listener: SignalUpdateListener[T_super] | SignalChangeListener[T_super]) -> None:
        self.__on_helper(listener, self.__change_listeners)
    
    def __on_helper(self, listener: SignalUpdateListener[T_super] | SignalChangeListener[T_super], list_of_listeners: list[SignalChangeListener[T_super]]) -> None:
        sig = signature(listener)
        if len(sig.parameters) == 1:
            original_listener = listener
            listener = lambda old_value, new_value: original_listener(new_value)
        list_of_listeners.append(listener)
    
    def bind_value_from(self, from_signal: "Signal[T_extends]") -> None:
        from_signal.on_change(lambda n: self._set_value(n))
        self._set_value(from_signal.get_value())
    
    def bind_value_to(self, to_signal: "Signal[T_super]") -> None:
        self.on_change(lambda n: to_signal._set_value(n))
        to_signal._set_value(self.get_value())