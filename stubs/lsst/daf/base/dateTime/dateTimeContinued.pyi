from .dateTime import DateTime as DateTime
from lsst.utils import continueClass as continueClass
from typing import Any, Optional

class DateTime:
    def toPython(self, timescale: Optional[Any] = ...): ...
    def __reduce__(self): ...
