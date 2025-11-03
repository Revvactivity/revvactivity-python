from typing import Generic, Protocol, TypeVar

from revvactivity_python.signal.functions.signal_function import SignalFunction


T = TypeVar("T")

class SignalDerived(Generic[T], SignalFunction, Protocol[T]):
    def __call__(self) -> T:
        ...
    
    def get(self) -> T:
        return self()