from typing import Any, Self, Iterable, Callable, overload

from ._node import Node

    
class DoublyLinkedList:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable) -> None: ...

    def __init__(self, iterable = None) -> None:
        self.__length: int = 0

        if iterable:
            self.extend(iterable)
            return

        self.head: Node | None = None
        self.tail: Node | None = None

    def __repr__(self) -> str:
        return f'DoublyLinkedList(head={self.head}, tail={self.tail}, length={self.__length})'
    
    @overload
    def __str__(self) -> str: ...
    @overload
    def __str__(self, reversed: bool) -> str: ...

    def __str__(self, reversed = False):
        list = ''
        get_node = lambda node: node.previous if reversed is True else lambda node: node.next

        if reversed is True:
            get_node = lambda node: node.previous
            node = self.tail
        else:
            get_node = lambda node: node.next
            node = self.head

        while node:
            list += f'{node}, '
            node = get_node(node)

        return f'DoublyLinkedList([{list[:-2]}])'
    
    def __iter__(self) -> Self:
        self.current = self.head

        return self

    def __next__(self) -> Node | StopIteration:
        if self.current:
            current = self.current
            self.current = self.current.next

            return current
        else:
            raise StopIteration
        
    def __len__(self) -> int:
        return self.length()
    
    def __setitem__(self, index: int, data: Any) -> None:
        if self.is_empty() or index == self.length():
            self.append(data)
            return

        if index > self.length() - 1:
            raise IndexError('doubly linked list assignment index out of range')
        
        node: Node = self.__getitem__(index, True)
        node.data = data

    def __delitem__(self, index: int) -> None:
        self.pop(index)
        
    @overload
    def __getitem__(self, index: int) -> Any: ...
    @overload
    def __getitem__(self, index: int, returnNode: bool) -> Node: ...
    @overload
    def __getitem__(self, index: slice) -> 'DoublyLinkedList': ...

    def __getitem__(self, index, returnNode = False):
        if isinstance(index, slice):
            start = index.start or 0
            stop = index.stop or self.length()
            step = index.step or 1

            if step < 0:
                get_node = lambda node: node.previous
                node = self.__getitem__(stop - 1, True)
            else:
                get_node = lambda node: node.next
                node = self.__getitem__(start, True)

            list = DoublyLinkedList()
            stop -= start
            i = 0

            while i < stop:
                if i % step == 0:
                    list.append(node)

                node = get_node(node)
                i += 1

            return list
        
        if isinstance(index, int):
            if index < 0:
                index += self.length()

            if index < 0 or (index >= self.length()):
                raise IndexError('doubly linked list index out of range')
            
            if index == self.length() - 1:
                return self.tail
            
            middle = self.length() // 2

            if index < middle:
                node = self.head

                for _ in range(index):
                    node = node.next
            else:
                node = self.tail

                for _ in range((self.length() - 1) - index):
                    node = node.previous

            if not node:
                raise RuntimeError()

            return node if returnNode is True else node.data
        
        raise TypeError('doubly linked list indices must be integers or slices')
    
    def length(self) -> int:
        return self.__length

    def is_empty(self) -> bool:
        return True if self.length() == 0 else False
        
    @overload
    def print(self) -> None: ...
    @overload
    def print(self, reversed: bool) -> None: ...

    def print(self, reversed = False):
        if reversed is True:
            print(self.__str__(True))
            return

        print(self.__str__())

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            if not self.tail:
                raise RuntimeError()

            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.__length += 1

    def extend(self, iterable: Iterable):
        for item in iterable:
            self.append(item)

    def insert(self, index: int, data: Any) -> None:
        if self.is_empty() or index == self.length():
            self.append(data)
            return
        
        if index > self.length():
            raise IndexError('doubly linked list index out of range')
        
        new_node = Node(data)
        self.__length += 1

        if index == 0:
            if not self.head:
                raise RuntimeError()
            
            new_node.next = self.head
            self.head.previous = self.head
            self.head = new_node
            return
        
        previous_node: Node = self.__getitem__(index - 1, True)
        new_node.next = previous_node.next
        new_node.previous = previous_node
        previous_node.next = new_node

        next_node = new_node.next
        next_node.previous = new_node
        next_node.next = next_node.next

    def remove(self, value: Any) -> None:
        if not self.head:
            raise ValueError('remove from empty doubly linked list')
        
        if self.head.data == value:
            self.pop(0)
            return
        
        node = self.head.next

        if node:
            previous_node = self.head

            while node:
                if node.data == value:
                    self.__length -= 1

                    if node is self.tail:
                        previous_node.next = None
                        self.tail = previous_node
                        return
                    
                    next_node = node.next
                    next_node.previous = previous_node
                    previous_node.next = next_node
                    return

                previous_node = node
                node = node.next
        
        raise ValueError(f'{value} is not in doubly linked list')

    @overload
    def pop(self) -> Node: ...
    @overload
    def pop(self, index: int) -> Node: ...

    def pop(self, index = -1):
        if self.is_empty() or not self.head:
            raise IndexError('pop from empty doubly linked list')        

        if index >= self.length():
            raise IndexError('doubly linked list index out of range') 
        
        if self.length() == 1:
            target_node = self.head
            self.clear()
            return target_node

        if index == 0:
            target_node = self.head
            self.head = target_node.next
            self.head.previous = None # type: ignore[union-attr]
            self.__length -= 1

            return target_node
        
        target_node = self.__getitem__(index, True)
        previous_node = target_node.previous
        self.__length -= 1

        if target_node is self.tail:
            previous_node.next = None
            self.tail = previous_node

            return target_node

        next_node = target_node.next  
        next_node.previous = previous_node
        previous_node.next = next_node
   
        return target_node
    
    def clear(self) -> None:
        self.head, self.tail = None, None    
        self.__length = 0

    @overload
    def index(self, value: Any) -> int: ...
    @overload
    def index(self, value: Any, start: int) -> int: ...
    @overload
    def index(self, value: Any, stop: int) -> int: ...
    @overload
    def index(self, value: Any, start: int, stop: int) -> int: ...

    def index(self, value, start=None, stop=None):
        node = self.head

        if not self.head:
            raise ValueError(f'{value} is not in doubly linked list')
        
        index = 0
        start = start or 0
        stop = stop or self.length()

        while index < stop and node:
            if index > start and node.data == value:
                return index

            node = node.next
            index += 1

        raise ValueError(f'{value} is not in doubly linked list')

    def count(self, value: Any) -> int:
        node = self.head

        if not node:
            return 0
        
        count = 0

        while node:
            if node.data == value:
                count += 1

            node = node.next

        return count

    @overload
    def sort(self) -> None: ...
    @overload
    def sort(self, reverse: bool) -> None: ...
    @overload
    def sort(self, key: Callable, reverse: bool) -> None: ...

    # TODO: Implementar outro método de ordenação 
    def sort(self, key=None, reverse=False):
        if self.length() <= 1:
            return
            
        node = self.head
        next_node = node.next

        if isinstance(key, Callable):
            if reverse is True:
                sorting_order = lambda node1, node2: key(node1.data) > key(node2.data)
            else:
                sorting_order = lambda node1, node2: key(node1.data) < key(node2.data)
        else:
            if reverse is True:
                sorting_order = lambda node1, node2: node1.data > node2.data
            else:
                sorting_order = lambda node1, node2: node1.data < node2.data

        for _ in range(self.length() - 1):   
            while next_node:
                if sorting_order(next_node, node):
                    node.data, next_node.data = next_node.data, node.data
                
                next_node = next_node.next

            node = node.next # type: ignore[assignment]
            next_node = node.next 

    def reverse(self) -> None:
        if not self.head:
            return
        
        node = self.head

        while node:
            node.previous, node.next = node.next, node.previous
            node = node.previous

        self.head, self.tail = self.tail, self.head

    def copy(self) -> 'DoublyLinkedList':
        return self[::]