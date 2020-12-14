from ._base import Catalog as Catalog
from ._table import SourceCatalog as SourceCatalog, SourceTable as SourceTable
from lsst.utils import continueClass as continueClass
from typing import Any

class SourceCatalog:
    def getChildren(self, parent: Any, *args: Any): ...
