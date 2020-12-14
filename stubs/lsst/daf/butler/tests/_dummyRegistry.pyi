from lsst.daf.butler import DatasetRef, DimensionUniverse, ddl
from lsst.daf.butler.registry.interfaces import Database, DatasetRecordStorageManager, DatastoreRegistryBridge, DatastoreRegistryBridgeManager, OpaqueTableStorage, OpaqueTableStorageManager, StaticTablesContext, VersionTuple
from typing import Any, Iterable, Iterator, Optional, Type

class DummyOpaqueTableStorage(OpaqueTableStorage):
    def __init__(self, name: str, spec: ddl.TableSpec) -> None: ...
    def insert(self, *data: dict) -> Any: ...
    def fetch(self, **where: Any) -> Iterator[dict]: ...
    def delete(self, **where: Any) -> Any: ...

class DummyOpaqueTableStorageManager(OpaqueTableStorageManager):
    def __init__(self) -> None: ...
    @classmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext) -> OpaqueTableStorageManager: ...
    def get(self, name: str) -> Optional[OpaqueTableStorage]: ...
    def register(self, name: str, spec: ddl.TableSpec) -> OpaqueTableStorage: ...
    @classmethod
    def currentVersion(cls: Any) -> Optional[VersionTuple]: ...
    def schemaDigest(self) -> Optional[str]: ...

class DummyDatastoreRegistryBridgeManager(DatastoreRegistryBridgeManager):
    def __init__(self, opaque: OpaqueTableStorageManager, universe: DimensionUniverse) -> None: ...
    @classmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext, opaque: OpaqueTableStorageManager, datasets: Type[DatasetRecordStorageManager], universe: DimensionUniverse) -> DatastoreRegistryBridgeManager: ...
    def refresh(self) -> None: ...
    def register(self, name: str, *, ephemeral: bool=...) -> DatastoreRegistryBridge: ...
    def findDatastores(self, ref: DatasetRef) -> Iterable[str]: ...
    @classmethod
    def currentVersion(cls: Any) -> Optional[VersionTuple]: ...
    def schemaDigest(self) -> Optional[str]: ...

class DummyRegistry:
    dimensions: Any = ...
    def __init__(self) -> None: ...
    def getDatastoreBridgeManager(self): ...
