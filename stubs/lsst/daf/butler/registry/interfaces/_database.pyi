import abc
import sqlalchemy
from ...core import TimespanDatabaseRepresentation, ddl
from .._exceptions import ConflictingDefinitionError
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple, Type

class ReadOnlyDatabaseError(RuntimeError): ...
class DatabaseConflictError(ConflictingDefinitionError): ...
class SchemaAlreadyDefinedError(RuntimeError): ...

class StaticTablesContext:
    def __init__(self, db: Database) -> None: ...
    def addTable(self, name: str, spec: ddl.TableSpec) -> sqlalchemy.schema.Table: ...
    def addTableTuple(self, specs: Tuple[ddl.TableSpec, ...]) -> Tuple[sqlalchemy.schema.Table, ...]: ...
    def addInitializer(self, initializer: Callable[[Database], None]) -> None: ...

class Database(ABC, metaclass=abc.ABCMeta):
    origin: Any = ...
    namespace: Any = ...
    def __init__(self, origin: int, connection: sqlalchemy.engine.Connection, *, namespace: Optional[str]=...) -> None: ...
    @classmethod
    def makeDefaultUri(cls: Any, root: str) -> Optional[str]: ...
    @classmethod
    def fromUri(cls: Any, uri: str, origin: int, *, namespace: Optional[str]=..., writeable: bool=...) -> Database: ...
    @classmethod
    @abstractmethod
    def connect(cls: Any, uri: str, *, writeable: bool=...) -> sqlalchemy.engine.Connection: ...
    @classmethod
    @abstractmethod
    def fromConnection(cls: Any, connection: sqlalchemy.engine.Connection, origin: int, *, namespace: Optional[str]=..., writeable: bool=...) -> Database: ...
    def transaction(self, *, interrupting: bool=..., savepoint: bool=..., lock: Iterable[sqlalchemy.schema.Table]=...) -> Iterator: ...
    def isTableWriteable(self, table: sqlalchemy.schema.Table) -> bool: ...
    def assertTableWriteable(self, table: sqlalchemy.schema.Table, msg: str) -> None: ...
    def declareStaticTables(self, create: bool) -> Iterator[StaticTablesContext]: ...
    @abstractmethod
    def isWriteable(self) -> bool: ...
    @property
    def dialect(self) -> sqlalchemy.engine.Dialect: ...
    def shrinkDatabaseEntityName(self, original: str) -> str: ...
    def expandDatabaseEntityName(self, shrunk: str) -> str: ...
    def ensureTableExists(self, name: str, spec: ddl.TableSpec) -> sqlalchemy.schema.Table: ...
    def getExistingTable(self, name: str, spec: ddl.TableSpec) -> Optional[sqlalchemy.schema.Table]: ...
    def makeTemporaryTable(self, spec: ddl.TableSpec, name: Optional[str]=...) -> sqlalchemy.schema.Table: ...
    def dropTemporaryTable(self, table: sqlalchemy.schema.Table) -> None: ...
    @classmethod
    def getTimespanRepresentation(cls: Any) -> Type[TimespanDatabaseRepresentation]: ...
    def sync(self, table: sqlalchemy.schema.Table, keys: Dict[str, Any], *, compared: Optional[Dict[str, Any]]=..., extra: Optional[Dict[str, Any]]=..., returning: Optional[Sequence[str]]=...) -> Tuple[Optional[Dict[str, Any]], bool]: ...
    def insert(self, table: sqlalchemy.schema.Table, *rows: dict, returnIds: bool=..., select: Optional[sqlalchemy.sql.Select]=..., names: Optional[Iterable[str]]=...) -> Optional[List[int]]: ...
    @abstractmethod
    def replace(self, table: sqlalchemy.schema.Table, *rows: dict) -> None: ...
    @abstractmethod
    def ensure(self, table: sqlalchemy.schema.Table, *rows: dict) -> int: ...
    def delete(self, table: sqlalchemy.schema.Table, columns: Iterable[str], *rows: dict) -> int: ...
    def update(self, table: sqlalchemy.schema.Table, where: Dict[str, str], *rows: dict) -> int: ...
    def query(self, sql: sqlalchemy.sql.FromClause, *args: Any, **kwds: Any) -> sqlalchemy.engine.ResultProxy: ...
