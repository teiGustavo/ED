from typing import Any, Iterable, Iterator, overload

from ._queueinterface import QueueInterface
from linkedlists import SinglyLinkedList


class Queue(QueueInterface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__items: SinglyLinkedList = SinglyLinkedList(iterable)

    def __repr__(self) -> str:
        q = f'{self.__items}'.replace('SinglyLinkedList([', '').replace('])', '')
        
        return f'Queue([{q}])'

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
            self.__items.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        
        return self.__items.pop(0)