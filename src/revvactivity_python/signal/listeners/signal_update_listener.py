from typing import Protocol, TypeVar

from revvactivity_python.signal.listeners.signal_listener import SignalListener


T = TypeVar("T")

class SignalUpdateListener(SignalListener[T], Protocol[T]):
    def __call__(self, value: T) -> None:
        ...
    
    def on_update(self, value: T) -> None:
        return self()