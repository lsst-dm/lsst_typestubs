import string
from lsst.daf.butler.core.config import Config as Config
from typing import Any, Optional

class BpsFormatter(string.Formatter):
    def get_field(self, field_name: Any, args: Any, kwargs: Any): ...
    def get_value(self, key: Any, args: Any, kwargs: Any): ...

class BpsConfig(Config):
    search_order: Any = ...
    formatter: Any = ...
    def __init__(self, other: Any, search_order: Optional[Any] = ...) -> None: ...
    def copy(self): ...
    def __getitem__(self, name: Any): ...
    def __contains__(self, name: Any): ...
    def search(self, key: Any, opt: Optional[Any] = ...): ...
