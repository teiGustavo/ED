from typing import Any, Iterable, Iterator, overload

from ._stackinterface import StackInterface
from linkedlists import DoublyLinkedList

class Stack(StackInterface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__items: DoublyLinkedList = DoublyLinkedList(iterable)

    def __repr__(self) -> str:
        q = f'{self.__items}'.replace('DoublyLinkedList([', '').replace('])', '')
        
        return f'Stack([{q}])'

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

    def push(self, *items: Any) -> None:
        for item in items:
            self.__items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('pop from empty stack')
        
        return self.__items.pop()