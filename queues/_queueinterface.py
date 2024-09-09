from abc import	ABC, abstractmethod
from typing import Any, Iterator, overload


class QueueInterface(ABC):
    @abstractmethod
    def __repr__(self) -> str: ...

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __iter__(self) -> Iterator: ...

    @abstractmethod
    def __getitem__(self, index: int) -> Any: ...

    @abstractmethod
    def length(self) -> int: ...

    @abstractmethod
    def is_empty(self) -> int: ...

    @abstractmethod
    def enqueue(self, *items: Any) -> None: ...

    @abstractmethod
    def dequeue(self) -> Any: ...