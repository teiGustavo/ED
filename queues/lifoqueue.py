from typing import Any, Iterable, Iterator, overload

from ._queueinterface import QueueInterface
from stacks import Stack


class LifoQueue(QueueInterface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__items: Stack = Stack(iterable)

    def __repr__(self) -> str:
        q = f'{self.__items}'.replace('Stack([', '').replace('])', '')
        
        return f'LifoQueue([{q}])'

    def __str__(self) -> str:
        return self.__repr__()
    
    def __len__(self) -> int:
        return self.__items.length()
    
    def __iter__(self) -> Iterator:
        return self.__items.__iter__()
    
    def __getitem__(self, index: int) -> Any:
        return self.__items[index]
    
    def length(self) -> int:
        return self.__len__()
    
    def is_empty(self) -> bool:
        return self.__items.is_empty()

    def enqueue(self, *items: Any) -> None:
        for item in items:
            self.__items.push(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError('dequeue from empty lifo queue')
        
        return self.__items.pop()