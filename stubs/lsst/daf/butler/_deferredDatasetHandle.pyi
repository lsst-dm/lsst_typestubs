from ._butler import Butler
from .core import DataCoordinate, DatasetRef
from typing import Any, Optional

class DeferredDatasetHandle:
    def get(self, *, component: Optional[str]=..., parameters: Optional[dict]=..., **kwargs: dict) -> Any: ...
    @property
    def dataId(self) -> DataCoordinate: ...
    butler: Butler
    ref: DatasetRef
    parameters: Optional[dict]
    def __init__(self, butler: Any, ref: Any, parameters: Any) -> None: ...
