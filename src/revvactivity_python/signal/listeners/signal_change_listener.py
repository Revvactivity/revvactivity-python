from typing import Protocol, TypeVar

from revvactivity_python.signal.listeners.signal_listener import SignalListener


T = TypeVar("T")

class SignalChangeListener(SignalListener[T], Protocol[T]):
    def __call__(self, old_value: T, new_value: T) -> None:
        ...