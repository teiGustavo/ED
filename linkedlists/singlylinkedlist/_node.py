from typing import Any, overload

from .._basenode import BaseNode


class Node(BaseNode):
    @overload
    def __init__(self, data: Any, next: 'Node') -> None : ...
    @overload
    def __init__(self, data: Any, next: None = None) -> None : ...

    def __init__(self, data, next = None):
        super().__init__(data)
      
        if not isinstance(next, Node | None):
            raise TypeError('Node.next must be Node or None')

        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f'Node(data={self.data}, next={self.next})'