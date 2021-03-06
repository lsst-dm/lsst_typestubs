import abc
import re
from ..translators import TranslatorFactory
from .parser import PathElementParser
from .scanner import DirectoryScanner, PathElementHandler
from abc import ABC, abstractmethod
from lsst.daf.butler import DimensionUniverse, FormatterParameter, StorageClass
from typing import Any, Dict, List, Optional, Tuple

class BuilderNode(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...
    @abstractmethod
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...

class BuilderInput(BuilderNode, metaclass=abc.ABCMeta):
    template: Any = ...
    keys: Any = ...
    elements: Any = ...
    def __init__(self, template: str, keys: Dict[str, type]) -> None: ...

class BuilderSkipInput(BuilderInput):
    def __init__(self, template: str, keys: Dict[str, type], message: Optional[str]=..., *, isForFiles: bool=...) -> None: ...
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...

class BuilderTargetInput(BuilderInput):
    datasetType: Any = ...
    def __init__(self, datasetTypeName: str, template: str, keys: Dict[str, type], storageClass: StorageClass, universe: DimensionUniverse, formatter: FormatterParameter, translatorFactory: TranslatorFactory, *, targetHandler: Optional[PathElementHandler]=..., **kwargs: Any) -> None: ...
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...

class BuilderPrunedTree(BuilderNode):
    def __init__(self, messages: List[str]) -> None: ...
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...

class BuilderDuplicateInputs(BuilderNode):
    def __init__(self, old: BuilderInput, new: BuilderInput) -> None: ...
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...

class BuilderTree(BuilderNode):
    def __init__(self) -> None: ...
    def insert(self, level: int, leaf: BuilderInput) -> Any: ...
    def fill(self, scanner: DirectoryScanner, allKeys: Dict[str, type], previousKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> Any: ...
    def prune(self) -> Tuple[BuilderNode, List[str], bool]: ...
    def build(self, parser: PathElementParser, allKeys: Dict[str, type], cumulativeKeys: Dict[str, type], fileIgnoreRegEx: Optional[re.Pattern], dirIgnoreRegEx: Optional[re.Pattern]) -> PathElementHandler: ...
