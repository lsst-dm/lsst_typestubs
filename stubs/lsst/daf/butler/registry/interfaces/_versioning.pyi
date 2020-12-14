import abc
from abc import ABC, abstractmethod
from typing import Any, NamedTuple, Optional

class VersionTuple(NamedTuple):
    major: int
    minor: int
    patch: int
    @classmethod
    def fromString(cls: Any, versionStr: str) -> VersionTuple: ...

class VersionedExtension(ABC, metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def currentVersion(cls: Any) -> Optional[VersionTuple]: ...
    @classmethod
    def extensionName(cls: Any) -> str: ...
    @abstractmethod
    def schemaDigest(self) -> Optional[str]: ...
