import sqlalchemy.sql
from ...core import DatasetType, Dimension, DimensionElement
from ...core.named import NamedValueAbstractSet
from ._query import Query
from ._structs import DatasetQueryColumns, QuerySummary, RegistryManagers
from typing import Any, Iterable, List, Optional

class QueryBuilder:
    summary: Any = ...
    def __init__(self, summary: QuerySummary, managers: RegistryManagers) -> None: ...
    def hasDimensionKey(self, dimension: Dimension) -> bool: ...
    def joinDimensionElement(self, element: DimensionElement) -> None: ...
    def joinDataset(self, datasetType: DatasetType, collections: Any, *, isResult: bool=..., findFirst: bool=...) -> bool: ...
    def joinTable(self, table: sqlalchemy.sql.FromClause, dimensions: NamedValueAbstractSet[Dimension], *, datasets: Optional[DatasetQueryColumns]=...) -> None: ...
    def startJoin(self, table: sqlalchemy.sql.FromClause, dimensions: Iterable[Dimension], columnNames: Iterable[str]) -> List[sqlalchemy.sql.ColumnElement]: ...
    def finishJoin(self, table: sqlalchemy.sql.FromClause, joinOn: List[sqlalchemy.sql.ColumnElement]) -> None: ...
    def finish(self, joinMissing: bool=...) -> Query: ...
