from typing import Any, overload, Iterable, override, Callable

from ...singlylinkedlist.singlylinkedlist import SinglyLinkedList
from ...singlylinkedlist._node import Node


class SinglyLinkedDescendingOrderedList(SinglyLinkedList):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None):
        super().__init__()

        self.extend(iterable)

    @overload
    def __str__(self) -> str: ...
    @overload
    def __str__(self, reversed: bool) -> str: ...

    def __str__(self, reverse = None):
        return super().__str__(reverse).replace('SinglyLinkedList', 'SinglyLinkedOrderedList')
    
    @override
    def __setitem__(self, index: int, data: Any) -> None:
        raise RuntimeError('method not allowed in singly linked ordered list')
    
    @override
    def append(self, data: Any) -> None:
        if self.is_empty():
            super().append(data)
            return
        
        if not self.head or not self.tail:
            raise RuntimeError()

        if not type(data) == type(self.head.data):
            raise TypeError('data types must be the same')

        new_node = Node(data)
        previous_node = None
        node = self.head

        while node:
            if data > node.data:
                if node is self.head:
                    super().insert(0, data)
                    return
                
                if not previous_node or not previous_node.next:
                    raise RuntimeError()
                
                new_node.next = node
                previous_node.next = new_node
                self.increase_length()
                return

            previous_node = node
            node = node.next

        self.tail.next = new_node
        self.increase_length()
    
    @override
    def extend(self, iterable: Iterable):
        for item in iterable:
            self.append(item)

    @override
    def insert(self, index, data) -> None:
        raise RuntimeError('method not allowed in singly linked ordered list')
    
    @override
    def sort(self):
        raise RuntimeError('singly linked ordered list is already sorted')