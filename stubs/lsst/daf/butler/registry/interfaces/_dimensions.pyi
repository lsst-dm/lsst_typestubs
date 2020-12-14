import abc
import sqlalchemy
from ...core import DataCoordinateIterable, DatabaseDimensionElement, DimensionElement, DimensionGraph, DimensionRecord, DimensionUniverse, GovernorDimension, NamedKeyDict, NamedKeyMapping, SkyPixDimension, TimespanDatabaseRepresentation
from ..queries import QueryBuilder
from ._database import Database, StaticTablesContext
from ._versioning import VersionedExtension
from abc import ABC, abstractmethod
from typing import AbstractSet, Any, Callable, Iterable, Mapping, Optional, Tuple, Union

OverlapSide = Union[SkyPixDimension, Tuple[DatabaseDimensionElement, str]]

class DimensionRecordStorage(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def element(self) -> DimensionElement: ...
    @abstractmethod
    def clearCaches(self) -> None: ...
    @abstractmethod
    def join(self, builder: QueryBuilder, *, regions: Optional[NamedKeyDict[DimensionElement, sqlalchemy.sql.ColumnElement]]=..., timespans: Optional[NamedKeyDict[DimensionElement, TimespanDatabaseRepresentation]]=...) -> sqlalchemy.sql.FromClause: ...
    @abstractmethod
    def insert(self, *records: DimensionRecord) -> None: ...
    @abstractmethod
    def sync(self, record: DimensionRecord) -> bool: ...
    @abstractmethod
    def fetch(self, dataIds: DataCoordinateIterable) -> Iterable[DimensionRecord]: ...
    @abstractmethod
    def digestTables(self) -> Iterable[sqlalchemy.schema.Table]: ...

class GovernorDimensionRecordStorage(DimensionRecordStorage, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, dimension: GovernorDimension, *, context: Optional[StaticTablesContext]=..., config: Mapping[str, Any]) -> GovernorDimensionRecordStorage: ...
    @property
    @abstractmethod
    def element(self) -> GovernorDimension: ...
    @abstractmethod
    def refresh(self) -> None: ...
    @property
    @abstractmethod
    def values(self) -> AbstractSet[str]: ...
    @property
    @abstractmethod
    def table(self) -> sqlalchemy.schema.Table: ...
    @abstractmethod
    def registerInsertionListener(self, callback: Callable[[DimensionRecord], None]) -> None: ...

class SkyPixDimensionRecordStorage(DimensionRecordStorage, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def element(self) -> SkyPixDimension: ...

class DatabaseDimensionRecordStorage(DimensionRecordStorage, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, element: DatabaseDimensionElement, *, context: Optional[StaticTablesContext]=..., config: Mapping[str, Any], governors: NamedKeyMapping[GovernorDimension, GovernorDimensionRecordStorage]) -> DatabaseDimensionRecordStorage: ...
    @property
    @abstractmethod
    def element(self) -> DatabaseDimensionElement: ...
    def connect(self, overlaps: DatabaseDimensionOverlapStorage) -> None: ...

class DatabaseDimensionOverlapStorage(ABC, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, elementStorage: Tuple[DatabaseDimensionRecordStorage, DatabaseDimensionRecordStorage], governorStorage: Tuple[GovernorDimensionRecordStorage, GovernorDimensionRecordStorage], context: Optional[StaticTablesContext]=...) -> DatabaseDimensionOverlapStorage: ...
    @property
    @abstractmethod
    def elements(self) -> Tuple[DatabaseDimensionElement, DatabaseDimensionElement]: ...
    @abstractmethod
    def digestTables(self) -> Iterable[sqlalchemy.schema.Table]: ...

class DimensionRecordStorageManager(VersionedExtension, metaclass=abc.ABCMeta):
    universe: Any = ...
    def __init__(self, universe: DimensionUniverse) -> None: ...
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext, universe: DimensionUniverse) -> DimensionRecordStorageManager: ...
    @abstractmethod
    def refresh(self) -> None: ...
    def __getitem__(self, element: DimensionElement) -> DimensionRecordStorage: ...
    @abstractmethod
    def get(self, element: DimensionElement) -> Optional[DimensionRecordStorage]: ...
    @abstractmethod
    def register(self, element: DimensionElement) -> DimensionRecordStorage: ...
    @abstractmethod
    def saveDimensionGraph(self, graph: DimensionGraph) -> int: ...
    @abstractmethod
    def loadDimensionGraph(self, key: int) -> DimensionGraph: ...
    @abstractmethod
    def clearCaches(self) -> None: ...
