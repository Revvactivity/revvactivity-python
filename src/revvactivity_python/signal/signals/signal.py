from typing import Generic, TypeVar


T = TypeVar("T")
T_extends = TypeVar("T_extends")
T_super = TypeVar("T_super")

class Signal(Generic[T]):
    def __init__(self, value: T | None = None):
        super().__init__()
        self.__value: T | None = value
    
    def get_value(self) -> T | None:
        return self.__value
    
    def _set_value(self, value: T | None) -> None:
        self.__value = value