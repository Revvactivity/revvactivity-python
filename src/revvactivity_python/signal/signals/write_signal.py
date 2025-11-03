from typing import Callable, TypeVar

from revvactivity_python.signal.signals.signal import Signal


T = TypeVar("T")

class WriteSignal(Signal[T]):
    def __init__(self, value: T | None = None):
        super().__init__(value)
    
    def set_value(self, value: T | None) -> None:
        super()._set_value(value)
    
    def update_value(self, update_function: Callable[[T | None], T | None]) -> None:
        self.set_value(update_function(self.get_value()))