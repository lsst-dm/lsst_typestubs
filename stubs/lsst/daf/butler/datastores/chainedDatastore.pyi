from lsst.daf.butler import ButlerURI, Config, Constraints, DatasetRef, DatasetType, Datastore, LookupKey, StorageClass
from lsst.daf.butler.registry.interfaces import DatastoreRegistryBridgeManager
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple, Union

class _IngestPrepData(Datastore.IngestPrepData):
    children: Any = ...
    def __init__(self, children: List[Tuple[Datastore, Datastore.IngestPrepData]]) -> None: ...

class ChainedDatastore(Datastore):
    defaultConfigFile: str = ...
    containerKey: str = ...
    datastores: List[Datastore]
    datastoreConstraints: Sequence[Optional[Constraints]]
    @classmethod
    def setConfigRoot(cls: Any, root: str, config: Config, full: Config, overwrite: bool=...) -> None: ...
    name: Any = ...
    isEphemeral: Any = ...
    def __init__(self, config: Union[Config, str], bridgeManager: DatastoreRegistryBridgeManager, butlerRoot: str=...) -> None: ...
    @property
    def names(self) -> Tuple[str, ...]: ...
    def exists(self, ref: DatasetRef) -> bool: ...
    def get(self, ref: DatasetRef, parameters: Optional[Mapping[str, Any]]=...) -> Any: ...
    def put(self, inMemoryDataset: Any, ref: DatasetRef) -> None: ...
    def getURIs(self, ref: DatasetRef, predict: bool=...) -> Tuple[Optional[ButlerURI], Dict[str, ButlerURI]]: ...
    def getURI(self, ref: DatasetRef, predict: bool=...) -> ButlerURI: ...
    def remove(self, ref: DatasetRef) -> None: ...
    def trash(self, ref: DatasetRef, ignore_errors: bool=...) -> None: ...
    def emptyTrash(self, ignore_errors: bool=...) -> None: ...
    def transfer(self, inputDatastore: Datastore, ref: DatasetRef) -> None: ...
    def validateConfiguration(self, entities: Iterable[Union[DatasetRef, DatasetType, StorageClass]], logFailures: bool=...) -> None: ...
    def validateKey(self, lookupKey: LookupKey, entity: Union[DatasetRef, DatasetType, StorageClass]) -> None: ...
    def getLookupKeys(self) -> Set[LookupKey]: ...
