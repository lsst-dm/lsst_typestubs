from .storageClass import StorageClass
from typing import Any, Dict, Iterable, Mapping, Optional, Set, Type

class DatasetComponent:
    name: str
    storageClass: StorageClass
    component: Any
    def __init__(self, name: Any, storageClass: Any, component: Any) -> None: ...

class StorageClassDelegate:
    storageClass: Any = ...
    def __init__(self, storageClass: StorageClass) -> None: ...
    def assemble(self, components: Dict[str, Any], pytype: Optional[Type]=...) -> Any: ...
    def getValidComponents(self, composite: Any) -> Dict[str, Any]: ...
    def getComponent(self, composite: Any, componentName: str) -> Any: ...
    def disassemble(self, composite: Any, subset: Optional[Iterable]=..., override: bool=...) -> Dict[str, Any]: ...
    def handleParameters(self, inMemoryDataset: Any, parameters: Optional[Mapping[str, Any]]=...) -> Any: ...
    @classmethod
    def selectResponsibleComponent(cls: Any, derivedComponent: str, fromComponents: Set[Optional[str]]) -> str: ...
