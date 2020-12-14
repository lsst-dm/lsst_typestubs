import abc
from ...core import DataCoordinate, DatasetRef, DatasetType, SimpleQuery, Timespan, ddl
from ._collections import CollectionManager, CollectionRecord, RunRecord
from ._database import Database, StaticTablesContext
from ._dimensions import DimensionRecordStorageManager
from ._versioning import VersionedExtension
from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator, Optional, Tuple

class DatasetRecordStorage(ABC, metaclass=abc.ABCMeta):
    datasetType: Any = ...
    def __init__(self, datasetType: DatasetType) -> None: ...
    @abstractmethod
    def insert(self, run: RunRecord, dataIds: Iterable[DataCoordinate]) -> Iterator[DatasetRef]: ...
    @abstractmethod
    def find(self, collection: CollectionRecord, dataId: DataCoordinate, timespan: Optional[Timespan]=...) -> Optional[DatasetRef]: ...
    @abstractmethod
    def delete(self, datasets: Iterable[DatasetRef]) -> None: ...
    @abstractmethod
    def associate(self, collection: CollectionRecord, datasets: Iterable[DatasetRef]) -> None: ...
    @abstractmethod
    def disassociate(self, collection: CollectionRecord, datasets: Iterable[DatasetRef]) -> None: ...
    @abstractmethod
    def certify(self, collection: CollectionRecord, datasets: Iterable[DatasetRef], timespan: Timespan) -> None: ...
    @abstractmethod
    def decertify(self, collection: CollectionRecord, timespan: Timespan, *, dataIds: Optional[Iterable[DataCoordinate]]=...) -> None: ...
    @abstractmethod
    def select(self, collection: CollectionRecord, dataId: SimpleQuery.Select.Or[DataCoordinate]=..., id: SimpleQuery.Select.Or[Optional[int]]=..., run: SimpleQuery.Select.Or[None]=..., timespan: SimpleQuery.Select.Or[Optional[Timespan]]=..., ingestDate: SimpleQuery.Select.Or[Optional[Timespan]]=...) -> Optional[SimpleQuery]: ...

class DatasetRecordStorageManager(VersionedExtension, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext, collections: CollectionManager, dimensions: DimensionRecordStorageManager) -> DatasetRecordStorageManager: ...
    @classmethod
    @abstractmethod
    def addDatasetForeignKey(cls: Any, tableSpec: ddl.TableSpec, *, name: str=..., constraint: bool=..., onDelete: Optional[str]=..., **kwargs: Any) -> ddl.FieldSpec: ...
    @abstractmethod
    def refresh(self) -> None: ...
    def __getitem__(self, name: str) -> DatasetRecordStorage: ...
    @abstractmethod
    def find(self, name: str) -> Optional[DatasetRecordStorage]: ...
    @abstractmethod
    def register(self, datasetType: DatasetType) -> Tuple[DatasetRecordStorage, bool]: ...
    @abstractmethod
    def remove(self, name: str) -> None: ...
    @abstractmethod
    def __iter__(self) -> Iterator[DatasetType]: ...
    @abstractmethod
    def getDatasetRef(self, id: int) -> Optional[DatasetRef]: ...