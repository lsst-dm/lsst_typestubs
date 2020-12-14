from lsst.obs.base import CameraMapper
from typing import Any, Optional

class CompositeMapper(CameraMapper):
    packageName: str = ...
    def __init__(self, root: Any, policy: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def std_stdTestType(self, item: Any, dataId: Any): ...
    def bypass_bypassTestType(self, datasetType: Any, pythonType: Any, location: Any, dataId: Any): ...