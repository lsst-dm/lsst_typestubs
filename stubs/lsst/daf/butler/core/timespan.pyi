import abc
import astropy.utils.exceptions
import sqlalchemy
from . import ddl
from ._topology import TopologicalExtentDatabaseRepresentation
from abc import abstractmethod
from typing import Any, ClassVar, Dict, Iterator, Mapping, NamedTuple, Optional, Tuple, Type, Union

class Timespan(NamedTuple):
    begin: Optional[astropy.time.Time]
    end: Optional[astropy.time.Time]
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def overlaps(self, other: Timespan) -> Any: ...
    def intersection(*args: Timespan) -> Optional[Timespan]: ...
    def difference(self, other: Timespan) -> Iterator[Timespan]: ...

class TimespanDatabaseRepresentation(TopologicalExtentDatabaseRepresentation, metaclass=abc.ABCMeta):
    NAME: ClassVar[str] = ...
    Compound: ClassVar[Type[TimespanDatabaseRepresentation]]
    @classmethod
    @abstractmethod
    def makeFieldSpecs(cls: Any, nullable: bool, **kwargs: Any) -> Tuple[ddl.FieldSpec, ...]: ...
    @classmethod
    @abstractmethod
    def getFieldNames(cls: Any) -> Tuple[str, ...]: ...
    @classmethod
    @abstractmethod
    def update(cls: Any, timespan: Optional[Timespan], *, result: Optional[Dict[str, Any]]=...) -> Dict[str, Any]: ...
    @classmethod
    @abstractmethod
    def extract(cls: Any, mapping: Mapping[str, Any]) -> Optional[Timespan]: ...
    @classmethod
    def hasExclusionConstraint(cls: Any) -> bool: ...
    @abstractmethod
    def isNull(self) -> sqlalchemy.sql.ColumnElement: ...
    @abstractmethod
    def overlaps(self, other: Union[Timespan, _S]) -> sqlalchemy.sql.ColumnElement: ...

class _CompoundTimespanDatabaseRepresentation(TimespanDatabaseRepresentation):
    begin: Any = ...
    end: Any = ...
    def __init__(self, begin: sqlalchemy.sql.ColumnElement, end: sqlalchemy.sql.ColumnElement) -> None: ...
    @classmethod
    def makeFieldSpecs(cls: Any, nullable: bool, **kwargs: Any) -> Tuple[ddl.FieldSpec, ...]: ...
    @classmethod
    def getFieldNames(cls: Any) -> Tuple[str, ...]: ...
    @classmethod
    def update(cls: Any, timespan: Optional[Timespan], *, result: Optional[Dict[str, Any]]=...) -> Dict[str, Any]: ...
    @classmethod
    def extract(cls: Any, mapping: Mapping[str, Any]) -> Optional[Timespan]: ...
    @classmethod
    def fromSelectable(cls: Any, selectable: sqlalchemy.sql.FromClause) -> _CompoundTimespanDatabaseRepresentation: ...
    def isNull(self) -> sqlalchemy.sql.ColumnElement: ...
    def overlaps(self, other: Union[Timespan, _CompoundTimespanDatabaseRepresentation]) -> sqlalchemy.sql.ColumnElement: ...
