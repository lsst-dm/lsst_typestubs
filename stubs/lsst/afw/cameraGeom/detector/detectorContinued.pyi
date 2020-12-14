from .detector import DetectorBase as DetectorBase
from typing import Any, Optional

DetectorTypeValNameDict: Any
DetectorTypeNameValDict: Any

class DetectorBase:
    def __iter__(self) -> Any: ...
    def fromConfig(self, config: Optional[Any] = ..., numAmps: int = ...) -> None: ...
