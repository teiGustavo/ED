from typing import Any, Iterable, Iterator, Tuple, overload

from ._queueinterface import QueueInterface
from linkedlists import SinglyLinkedDescendingOrderedList
from linkedlists.singlylinkedlist import Node

class PriorityQueue(QueueInterface):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[int, Any]]) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__items: SinglyLinkedDescendingOrderedList = SinglyLinkedDescendingOrderedList(iterable)
        # self.__items.sort(key=lambda item: item[0], reverse=True)

    def __repr__(self) -> str:
        q = f'{self.__items}'.replace('SinglyLinkedOrderedList([', '').replace('])', '')
        
        return f'PriorityQueue([{q}])'

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

    @overload
    def enqueue(self,  item: Any, priority: int) -> None: ...
    @overload
    def enqueue(self, item: Tuple[int, Any]) -> None: ...

    def enqueue(self, item, priority = None):
        if not isinstance(item, Tuple):
            item = (priority, item)

        self.__items.append(item)
  
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError('dequeue from empty priority queue')
        
        return self.__items.pop(0)