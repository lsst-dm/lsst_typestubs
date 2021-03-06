from ..config import Config
from ..named import NamedValueAbstractSet
from ._coordinate import DataCoordinate
from ._database import DatabaseDimensionElement
from ._elements import Dimension, DimensionElement
from ._governor import GovernorDimension
from ._graph import DimensionGraph
from ._packer import DimensionPacker
from ._skypix import SkyPixSystem
from .construction import DimensionConstructionBuilder
from typing import Any, Iterable, List, Optional, Set, TypeVar, Union

E = TypeVar('E', bound=DimensionElement)

class DimensionUniverse:
    commonSkyPix: Any = ...
    empty: Any = ...
    def __new__(cls: Any, config: Optional[Config]=..., *, version: Optional[int]=..., builder: Optional[DimensionConstructionBuilder]=...) -> DimensionUniverse: ...
    def __getitem__(self, name: str) -> DimensionElement: ...
    def get(self, name: str, default: Optional[DimensionElement]=...) -> Optional[DimensionElement]: ...
    def getStaticElements(self) -> NamedValueAbstractSet[DimensionElement]: ...
    def getStaticDimensions(self) -> NamedValueAbstractSet[Dimension]: ...
    def getGovernorDimensions(self) -> NamedValueAbstractSet[GovernorDimension]: ...
    def getDatabaseElements(self) -> NamedValueAbstractSet[DatabaseDimensionElement]: ...
    @property
    def skypix(self) -> NamedValueAbstractSet[SkyPixSystem]: ...
    def getElementIndex(self, name: str) -> int: ...
    def getDimensionIndex(self, name: str) -> int: ...
    def expandDimensionNameSet(self, names: Set[str]) -> None: ...
    def extract(self, iterable: Iterable[Union[Dimension, str]]) -> DimensionGraph: ...
    def sorted(self, elements: Iterable[Union[E, str]], *, reverse: bool=...) -> List[E]: ...
    def makePacker(self, name: str, dataId: DataCoordinate) -> DimensionPacker: ...
    def getEncodeLength(self) -> int: ...
    def __reduce__(self) -> tuple: ...
    def __deepcopy__(self, memo: dict) -> DimensionUniverse: ...
