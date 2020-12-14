from ..dimensions import DataCoordinate, DimensionGraph
from ..named import NamedKeyDict
from .type import DatasetType
from typing import Any, Iterable, List, Optional

class AmbiguousDatasetError(Exception): ...

class DatasetRef:
    id: Any = ...
    datasetType: Any = ...
    hasParentId: Any = ...
    dataId: Any = ...
    run: Any = ...
    def __init__(self, datasetType: DatasetType, dataId: DataCoordinate, *, id: Optional[int]=..., run: Optional[str]=..., hasParentId: bool=..., conform: bool=...) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def dimensions(self) -> DimensionGraph: ...
    def __lt__(self, other: Any) -> bool: ...
    def __reduce__(self) -> tuple: ...
    def __deepcopy__(self, memo: dict) -> DatasetRef: ...
    def resolved(self, id: int, run: str) -> DatasetRef: ...
    def unresolved(self) -> DatasetRef: ...
    def expanded(self, dataId: DataCoordinate) -> DatasetRef: ...
    def isComponent(self) -> bool: ...
    def isComposite(self) -> bool: ...
    @staticmethod
    def groupByType(refs: Iterable[DatasetRef]) -> NamedKeyDict[DatasetType, List[DatasetRef]]: ...
    def getCheckedId(self) -> int: ...
    def makeComponentRef(self, name: str) -> DatasetRef: ...
