from typing import Any, Iterable, Iterator, Deque, overload
from collections import deque

from ._stackinterface import StackInterface

class SimpleStack(StackInterface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__items: Deque[Any] = deque(iterable)

    def __repr__(self) -> str:
        q = f'{self.__items}'.replace('deque([', '').replace('])', '')
        
        return f'SimpleStack([{q}])'

    def __str__(self) -> str:
        return self.__repr__()
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __iter__(self) -> Iterator:
        return self.__items.__iter__()
    
    def __getitem__(self, index: int) -> Any:
        return self.__items[index]
    
    def length(self) -> int:
        return self.__len__()
    
    def is_empty(self) -> bool:
        return True if self.__len__() == 0 else False

    def push(self, *items: Any) -> None:
        for item in items:
            self.__items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('pop from empty simple stack')
        
        return self.__items.pop()