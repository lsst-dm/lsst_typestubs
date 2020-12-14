import astropy.time
import sqlalchemy
from .config import Config
from .exceptions import ValidationError
from .timespan import TimespanDatabaseRepresentation
from lsst.sphgeom import ConvexPolygon
from typing import Any, Callable, Iterable, Optional, Tuple, Type, Union

class SchemaValidationError(ValidationError):
    @classmethod
    def translate(cls: Any, caught: Type[Exception], message: str) -> Callable: ...

class Base64Bytes(sqlalchemy.TypeDecorator):
    impl: Any = ...
    nbytes: Any = ...
    def __init__(self, nbytes: int, *args: Any, **kwargs: Any) -> None: ...
    def process_bind_param(self, value: Optional[bytes], dialect: sqlalchemy.engine.Dialect) -> Optional[str]: ...
    def process_result_value(self, value: Optional[str], dialect: sqlalchemy.engine.Dialect) -> Optional[bytes]: ...

class Base64Region(Base64Bytes):
    def process_bind_param(self, value: Optional[ConvexPolygon], dialect: sqlalchemy.engine.Dialect) -> Optional[str]: ...
    def process_result_value(self, value: Optional[str], dialect: sqlalchemy.engine.Dialect) -> Optional[ConvexPolygon]: ...

class AstropyTimeNsecTai(sqlalchemy.TypeDecorator):
    impl: Any = ...
    def process_bind_param(self, value: Optional[astropy.time.Time], dialect: sqlalchemy.engine.Dialect) -> Optional[int]: ...
    def process_result_value(self, value: Optional[int], dialect: sqlalchemy.engine.Dialect) -> Optional[astropy.time.Time]: ...

class FieldSpec:
    name: str
    dtype: type
    length: Optional[int] = ...
    nbytes: Optional[int] = ...
    primaryKey: bool = ...
    autoincrement: bool = ...
    nullable: bool = ...
    default: Any = ...
    doc: Optional[str] = ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @classmethod
    def fromConfig(cls: Any, config: Config, **kwds: Any) -> FieldSpec: ...
    def isStringType(self) -> bool: ...
    def getSizedColumnType(self) -> sqlalchemy.types.TypeEngine: ...
    def getPythonType(self) -> type: ...
    def __init__(self, name: Any, dtype: Any, length: Any, nbytes: Any, primaryKey: Any, autoincrement: Any, nullable: Any, default: Any, doc: Any) -> None: ...

class ForeignKeySpec:
    table: str
    source: Tuple[str, ...]
    target: Tuple[str, ...]
    onDelete: Optional[str] = ...
    addIndex: bool = ...
    @classmethod
    def fromConfig(cls: Any, config: Config) -> ForeignKeySpec: ...
    def __init__(self, table: Any, source: Any, target: Any, onDelete: Any, addIndex: Any) -> None: ...

class TableSpec:
    fields: Any = ...
    unique: Any = ...
    indexes: Any = ...
    foreignKeys: Any = ...
    exclusion: Any = ...
    recycleIds: Any = ...
    doc: Any = ...
    def __init__(self, fields: Iterable[FieldSpec], *, unique: Iterable[Tuple[str, ...]]=..., indexes: Iterable[Tuple[str, ...]]=..., foreignKeys: Iterable[ForeignKeySpec]=..., exclusion: Iterable[Tuple[Union[str, Type[TimespanDatabaseRepresentation]], ...]]=..., recycleIds: bool=..., doc: Optional[str]=...) -> None: ...
    @classmethod
    def fromConfig(cls: Any, config: Config) -> TableSpec: ...
