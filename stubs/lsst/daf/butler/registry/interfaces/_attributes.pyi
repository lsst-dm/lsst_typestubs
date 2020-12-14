import abc
from ._database import Database, StaticTablesContext
from ._versioning import VersionedExtension
from abc import abstractmethod
from typing import Any, Iterable, Optional, Tuple

class ButlerAttributeExistsError(RuntimeError): ...

class ButlerAttributeManager(VersionedExtension, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext) -> ButlerAttributeManager: ...
    @abstractmethod
    def get(self, name: str, default: Optional[str]=...) -> Optional[str]: ...
    @abstractmethod
    def set(self, name: str, value: str, *, force: bool=...) -> None: ...
    @abstractmethod
    def delete(self, name: str) -> bool: ...
    @abstractmethod
    def items(self) -> Iterable[Tuple[str, str]]: ...
    @abstractmethod
    def empty(self) -> bool: ...
