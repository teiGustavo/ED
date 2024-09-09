from typing import Any, overload

from .._basenode import BaseNode


class Node(BaseNode):
    @overload
    def __init__(self, data: Any, previous: 'Node', next: 'Node') -> None : ...
    @overload
    def __init__(self, data: Any, previous: 'Node', next: None = None) -> None : ...
    @overload
    def __init__(self, data: Any, next: 'Node', previous: None = None) -> None : ...
    @overload
    def __init__(self, data: Any, previous: None = None, next: None = None) -> None : ...

    def __init__(self, data, previous = None, next = None):
        super().__init__(data)
        
        if not isinstance(previous, Node | None):
            raise TypeError('Node.previous must be Node or None')
        
        if not isinstance(next, Node | None):
            raise TypeError('Node.next must be Node or None')

        self.data = data
        self.previous = previous
        self.next = next

    def __repr__(self) -> str:
        return f'Node(data={self.data}, previous={self.previous}, next={self.next})'