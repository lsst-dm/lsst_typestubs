from lsst.meas.algorithms import LoadReferenceObjectsConfig, LoadReferenceObjectsTask
from typing import Any, Optional

class LoadIndexedReferenceObjectsConfig(LoadReferenceObjectsConfig):
    ref_dataset_name: Any = ...

class LoadIndexedReferenceObjectsTask(LoadReferenceObjectsTask):
    ConfigClass: Any = ...
    dataset_config: Any = ...
    indexer: Any = ...
    ref_dataset_name: Any = ...
    butler: Any = ...
    def __init__(self, butler: Any, *args: Any, **kwargs: Any) -> None: ...
    def loadSkyCircle(self, ctrCoord: Any, radius: Any, filterName: Optional[Any] = ..., epoch: Optional[Any] = ..., centroids: bool = ...): ...
    def getShards(self, shardIdList: Any): ...