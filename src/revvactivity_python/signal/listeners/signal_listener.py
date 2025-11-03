from typing import Generic, Protocol, TypeVar


T = TypeVar("T")

class SignalListener(Generic[T], Protocol):
    ...