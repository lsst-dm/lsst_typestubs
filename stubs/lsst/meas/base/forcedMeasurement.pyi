from .baseMeasurement import BaseMeasurementConfig, BaseMeasurementPlugin, BaseMeasurementPluginConfig, BaseMeasurementTask
from typing import Any, Optional

class ForcedPluginConfig(BaseMeasurementPluginConfig): ...

class ForcedPlugin(BaseMeasurementPlugin):
    registry: Any = ...
    ConfigClass: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any, logName: Optional[Any] = ...) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...
    def measureN(self, measCat: Any, exposure: Any, refCat: Any, refWcs: Any) -> None: ...

class ForcedMeasurementConfig(BaseMeasurementConfig):
    plugins: Any = ...
    algorithms: Any = ...
    undeblended: Any = ...
    copyColumns: Any = ...
    checkUnitsParseStrict: Any = ...
    def setDefaults(self) -> None: ...

class ForcedMeasurementTask(BaseMeasurementTask):
    ConfigClass: Any = ...
    mapper: Any = ...
    schema: Any = ...
    def __init__(self, refSchema: Any, algMetadata: Optional[Any] = ..., **kwds: Any) -> None: ...
    def run(self, measCat: Any, exposure: Any, refCat: Any, refWcs: Any, exposureId: Optional[Any] = ..., beginOrder: Optional[Any] = ..., endOrder: Optional[Any] = ...) -> None: ...
    def generateMeasCat(self, exposure: Any, refCat: Any, refWcs: Any, idFactory: Optional[Any] = ...): ...
    def attachTransformedFootprints(self, sources: Any, refCat: Any, exposure: Any, refWcs: Any) -> None: ...
