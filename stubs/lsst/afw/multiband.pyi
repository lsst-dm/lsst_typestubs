import abc
from abc import ABC, abstractmethod
from typing import Any, Optional

class MultibandBase(ABC, metaclass=abc.ABCMeta):
    def __init__(self, filters: Any, singles: Any, bbox: Optional[Any] = ...) -> None: ...
    @abstractmethod
    def clone(self, deep: bool = ...) -> Any: ...
    @property
    def filters(self): ...
    @property
    def singles(self): ...
    def getBBox(self): ...
    def getXY0(self): ...
    @property
    def x0(self): ...
    @property
    def y0(self): ...
    @property
    def origin(self): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    def __len__(self): ...
    def __getitem__(self, args: Any): ...
    def __iter__(self) -> Any: ...
    def __next__(self): ...
    def setXY0(self, xy0: Any) -> None: ...
    def shiftedTo(self, xy0: Any): ...
    def shiftedBy(self, offset: Any): ...
