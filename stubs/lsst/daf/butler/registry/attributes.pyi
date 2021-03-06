import sqlalchemy
from .interfaces import ButlerAttributeManager, Database, StaticTablesContext, VersionTuple
from typing import Any, Iterable, Optional, Tuple

class MissingAttributesTableError(RuntimeError): ...

class DefaultButlerAttributeManager(ButlerAttributeManager):
    def __init__(self, db: Database, table: sqlalchemy.schema.Table) -> None: ...
    @classmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext) -> ButlerAttributeManager: ...
    def get(self, name: str, default: Optional[str]=...) -> Optional[str]: ...
    def set(self, name: str, value: str, *, force: bool=...) -> None: ...
    def delete(self, name: str) -> bool: ...
    def items(self) -> Iterable[Tuple[str, str]]: ...
    def empty(self) -> bool: ...
    @classmethod
    def currentVersion(cls: Any) -> Optional[VersionTuple]: ...
    def schemaDigest(self) -> Optional[str]: ...
