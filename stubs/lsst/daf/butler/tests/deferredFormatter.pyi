from ..core import Formatter as Formatter
from typing import Any, Optional

class DeferredFormatter(Formatter):
    def read(self, component: Optional[str]=...) -> Any: ...
    def write(self, inMemoryDataset: Any) -> str: ...
