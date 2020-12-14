from .datasets import DatasetRef
from .formatter import FormatterParameter
from typing import Any, List, Optional, Union

class FileDataset:
    refs: List[DatasetRef]
    path: str
    formatter: Optional[FormatterParameter]
    def __init__(self, path: str, refs: Union[DatasetRef, List[DatasetRef]], *, formatter: Optional[FormatterParameter]=...) -> None: ...
    def __lt__(self, other: Any) -> bool: ...
