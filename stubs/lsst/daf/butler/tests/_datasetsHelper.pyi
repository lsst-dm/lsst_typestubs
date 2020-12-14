from lsst.daf.butler.formatters.yaml import YamlFormatter
from typing import Any, Optional

class DatasetTestHelper:
    def makeDatasetRef(self, datasetTypeName: Any, dimensions: Any, storageClass: Any, dataId: Any, *, id: Optional[Any] = ..., run: Optional[Any] = ..., conform: bool = ...): ...

class DatastoreTestHelper:
    registry: Any = ...
    id: int = ...
    config: Any = ...
    def setUpDatastoreTests(self, registryClass: Any, configClass: Any) -> None: ...
    def makeDatastore(self, sub: Optional[Any] = ...): ...

class BadWriteFormatter(YamlFormatter): ...
class BadNoWriteFormatter(BadWriteFormatter): ...
class MultiDetectorFormatter(YamlFormatter): ...