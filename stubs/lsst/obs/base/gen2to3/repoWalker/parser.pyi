import abc
import re
from abc import ABC, abstractmethod
from lsst.log import Log
from typing import Any, ClassVar, Dict, Optional

class FormattableRegEx(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def format(self, dataId: dict) -> re.Pattern: ...

class FixedRegEx(FormattableRegEx):
    regex: Any = ...
    def __init__(self, regex: re.Pattern) -> None: ...
    def format(self, dataId: dict) -> re.Pattern: ...

class SubstitutableRegEx:
    def __init__(self) -> None: ...
    def addRegexTerm(self, regex: str) -> Any: ...
    def addSubstitutionTerm(self, template: str) -> Any: ...
    def format(self, dataId: dict) -> re.Pattern: ...
    def simplify(self) -> FormattableRegEx: ...

class PathElementParser:
    template: Any = ...
    keys: Any = ...
    regex: Any = ...
    def __init__(self, template: str, allKeys: Dict[str, type], *, previousKeys: Optional[Dict[str, type]]=...) -> None: ...
    TEMPLATE_RE: ClassVar[re.Pattern] = ...
    def parse(self, name: str, lastDataId: dict, *, log: Optional[Log]=...) -> Optional[dict]: ...
