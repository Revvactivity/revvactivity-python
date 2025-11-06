from typing import Protocol

from revvactivity_python.signal.functions.signal_function import SignalFunction


class SignalEffect(SignalFunction, Protocol):
    def __call__(self) -> None:
        ...