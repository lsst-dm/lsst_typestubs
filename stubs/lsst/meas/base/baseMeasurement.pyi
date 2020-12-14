import lsst.pex.config
from .pluginsBase import BasePlugin, BasePluginConfig
from typing import Any, Optional

class BaseMeasurementPluginConfig(BasePluginConfig):
    doMeasure: Any = ...
    doMeasureN: bool = ...

class BaseMeasurementPlugin(BasePlugin): ...

class SourceSlotConfig(lsst.pex.config.Config):
    Field: Any = ...
    centroid: Any = ...
    shape: Any = ...
    psfShape: Any = ...
    apFlux: Any = ...
    modelFlux: Any = ...
    psfFlux: Any = ...
    gaussianFlux: Any = ...
    calibFlux: Any = ...
    def setupSchema(self, schema: Any) -> None: ...

class BaseMeasurementConfig(lsst.pex.config.Config):
    slots: Any = ...
    doReplaceWithNoise: Any = ...
    noiseReplacer: Any = ...
    undeblendedPrefix: Any = ...
    def validate(self) -> None: ...

class BaseMeasurementTask(lsst.pipe.base.Task):
    ConfigClass: Any = ...
    plugins: Any = ...
    algMetadata: Any = ...
    undeblendedPlugins: Any = ...
    def __init__(self, algMetadata: Optional[Any] = ..., **kwds: Any) -> None: ...
    def getPluginLogName(self, pluginName: Any): ...
    def initializePlugins(self, **kwds: Any) -> None: ...
    def callMeasure(self, measRecord: Any, *args: Any, **kwds: Any) -> None: ...
    def doMeasurement(self, plugin: Any, measRecord: Any, *args: Any, **kwds: Any) -> None: ...
    def callMeasureN(self, measCat: Any, *args: Any, **kwds: Any) -> None: ...
    def doMeasurementN(self, plugin: Any, measCat: Any, *args: Any, **kwds: Any) -> None: ...
