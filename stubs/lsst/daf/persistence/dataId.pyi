from collections import UserDict
from typing import Any, Optional

class DataId(UserDict):
    tag: Any = ...
    def __init__(self, initialdata: Optional[Any] = ..., tag: Optional[Any] = ..., **kwargs: Any) -> None: ...
