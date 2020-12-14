import abc
from ...core import DimensionUniverse, Timespan, ddl
from .._collectionType import CollectionType
from ..wildcards import CollectionSearch
from ._database import Database, StaticTablesContext
from ._dimensions import DimensionRecordStorageManager
from ._versioning import VersionedExtension
from abc import abstractmethod
from typing import Any, Iterator, Optional

class MissingCollectionError(Exception): ...

class CollectionRecord:
    key: Any = ...
    name: Any = ...
    type: Any = ...
    def __init__(self, key: Any, name: str, type: CollectionType) -> None: ...

class RunRecord(CollectionRecord, metaclass=abc.ABCMeta):
    @abstractmethod
    def update(self, host: Optional[str]=..., timespan: Optional[Timespan]=...) -> None: ...
    @property
    @abstractmethod
    def host(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def timespan(self) -> Timespan: ...

class ChainedCollectionRecord(CollectionRecord, metaclass=abc.ABCMeta):
    def __init__(self, key: Any, name: str, universe: DimensionUniverse) -> None: ...
    @property
    def children(self) -> CollectionSearch: ...
    def update(self, manager: CollectionManager, children: CollectionSearch) -> None: ...
    def refresh(self, manager: CollectionManager) -> None: ...

class CollectionManager(VersionedExtension, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext, dimensions: DimensionRecordStorageManager) -> CollectionManager: ...
    @classmethod
    @abstractmethod
    def addCollectionForeignKey(cls: Any, tableSpec: ddl.TableSpec, *, prefix: str=..., onDelete: Optional[str]=..., constraint: bool=..., **kwargs: Any) -> ddl.FieldSpec: ...
    @classmethod
    @abstractmethod
    def addRunForeignKey(cls: Any, tableSpec: ddl.TableSpec, *, prefix: str=..., onDelete: Optional[str]=..., constraint: bool=..., **kwargs: Any) -> ddl.FieldSpec: ...
    @classmethod
    @abstractmethod
    def getCollectionForeignKeyName(cls: Any, prefix: str=...) -> str: ...
    @classmethod
    @abstractmethod
    def getRunForeignKeyName(cls: Any, prefix: str=...) -> str: ...
    @abstractmethod
    def refresh(self) -> None: ...
    @abstractmethod
    def register(self, name: str, type: CollectionType, doc: Optional[str]=...) -> CollectionRecord: ...
    @abstractmethod
    def remove(self, name: str) -> None: ...
    @abstractmethod
    def find(self, name: str) -> CollectionRecord: ...
    @abstractmethod
    def __getitem__(self, key: Any) -> CollectionRecord: ...
    @abstractmethod
    def __iter__(self) -> Iterator[CollectionRecord]: ...
    @abstractmethod
    def getDocumentation(self, key: Any) -> Optional[str]: ...
    @abstractmethod
    def setDocumentation(self, key: Any, doc: Optional[str]) -> None: ...
