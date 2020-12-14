import sqlalchemy
from collections import namedtuple
from lsst.daf.butler import DatasetType, DimensionUniverse, GovernorDimension, NamedKeyMapping, TimespanDatabaseRepresentation, ddl
from lsst.daf.butler.registry.interfaces import CollectionManager, Database, DimensionRecordStorageManager, StaticTablesContext
from typing import Any, Optional, Type

StaticDatasetTablesTuple = namedtuple('StaticDatasetTablesTuple', ['dataset_type', 'dataset'])

def addDatasetForeignKey(tableSpec: ddl.TableSpec, *, name: str=..., onDelete: Optional[str]=..., constraint: bool=..., **kwargs: Any) -> ddl.FieldSpec: ...
def makeStaticTableSpecs(collections: Type[CollectionManager], universe: DimensionUniverse) -> StaticDatasetTablesTuple: ...

class CollectionSummaryTables:
    datasetType: Any = ...
    dimensions: Any = ...
    def __init__(self, datasetType: _T, dimensions: NamedKeyMapping[GovernorDimension, _T]) -> None: ...
    @classmethod
    def initialize(cls: Any, db: Database, context: StaticTablesContext, collections: CollectionManager, dimensions: DimensionRecordStorageManager) -> CollectionSummaryTables[sqlalchemy.schema.Table]: ...
    @classmethod
    def makeTableSpecs(cls: Any, collections: CollectionManager, dimensions: DimensionRecordStorageManager) -> CollectionSummaryTables[ddl.TableSpec]: ...

def makeTagTableName(datasetType: DatasetType, dimensionsKey: int) -> str: ...
def makeCalibTableName(datasetType: DatasetType, dimensionsKey: int) -> str: ...
def makeTagTableSpec(datasetType: DatasetType, collections: Type[CollectionManager]) -> ddl.TableSpec: ...
def makeCalibTableSpec(datasetType: DatasetType, collections: Type[CollectionManager], tsRepr: Type[TimespanDatabaseRepresentation]) -> ddl.TableSpec: ...

# Names in __all__ with no definition:
#   StaticDatasetTablesTuple