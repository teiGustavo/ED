from typing import Any, overload


class BaseNode:
    def __init__(self, data: Any):
        self.data: Any = data

    def __repr__(self) -> str:
        return f'Node(data={self.data})'

    def __str__(self) -> str:
        return str(self.data)
    
    @overload
    def __eq__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __eq__(self, other: int) -> bool: ...
    @overload
    def __eq__(self, other: float) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...

    def __eq__(self, other):
        if isinstance(other, BaseNode):
            return self.data == other.data
        
        if isinstance(other, int | float):
            return self.data == other

        return False
    
    @overload
    def __ne__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __ne__(self, other: int) -> bool: ...
    @overload
    def __ne__(self, other: float) -> bool: ...
    @overload
    def __ne__(self, other: object) -> bool: ...

    def __ne__(self, other):
        return not self.__eq__(other)
    
    @overload
    def __lt__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __lt__(self, other: int) -> bool: ...
    @overload
    def __lt__(self, other: float) -> bool: ...
    @overload
    def __lt__(self, other: object) -> bool: ...

    def __lt__(self, other):
        if isinstance(other, BaseNode):
            return self.data < other.data
        
        if isinstance(other, int | float):
            return self.data < other
        
        return NotImplemented
    
    @overload
    def __le__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __le__(self, other: int) -> bool: ...
    @overload
    def __le__(self, other: float) -> bool: ...
    @overload
    def __le__(self, other: object) -> bool: ...

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    @overload
    def __gt__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __gt__(self, other: int) -> bool: ...
    @overload
    def __gt__(self, other: float) -> bool: ...
    @overload
    def __gt__(self, other: object) -> bool: ...

    def __gt__(self, other):
        return not self.__le__(other)
    
    @overload
    def __ge__(self, other: 'BaseNode') -> bool: ...
    @overload
    def __ge__(self, other: int) -> bool: ...
    @overload
    def __ge__(self, other: float) -> bool: ...
    @overload
    def __ge__(self, other: object) -> bool: ...

    def __ge__(self, other):
        return not self.__lt__(other)