from ..timespan import Timespan as Timespan
from .ref import DatasetRef as DatasetRef
from typing import Any, Optional

class DatasetAssociation:
    ref: DatasetRef
    collection: str
    timespan: Optional[Timespan]
    def __lt__(self, other: Any) -> bool: ...
    def __init__(self, ref: Any, collection: Any, timespan: Any) -> None: ...
