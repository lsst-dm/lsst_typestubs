from .baseMeasurement import BaseMeasurementPluginConfig
from .forcedMeasurement import ForcedPlugin, ForcedPluginConfig
from .sfm import SingleFramePlugin, SingleFramePluginConfig
from .wrappers import GenericPlugin
from typing import Any, Optional

class SingleFrameFPPositionConfig(SingleFramePluginConfig): ...

class SingleFrameFPPositionPlugin(SingleFramePlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    focalValue: Any = ...
    focalFlag: Any = ...
    detectorFlag: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

class SingleFrameJacobianConfig(SingleFramePluginConfig):
    pixelScale: Any = ...

class SingleFrameJacobianPlugin(SingleFramePlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    jacValue: Any = ...
    jacFlag: Any = ...
    scale: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

class VarianceConfig(BaseMeasurementPluginConfig):
    scale: Any = ...
    mask: Any = ...

class VariancePlugin(GenericPlugin):
    ConfigClass: Any = ...
    FAILURE_BAD_CENTROID: int = ...
    FAILURE_EMPTY_FOOTPRINT: int = ...
    @classmethod
    def getExecutionOrder(cls): ...
    varValue: Any = ...
    emptyFootprintFlag: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, center: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

SingleFrameVariancePlugin: Any
ForcedVariancePlugin: Any

class InputCountConfig(BaseMeasurementPluginConfig): ...

class InputCountPlugin(GenericPlugin):
    ConfigClass: Any = ...
    FAILURE_BAD_CENTROID: int = ...
    FAILURE_NO_INPUTS: int = ...
    @classmethod
    def getExecutionOrder(cls): ...
    numberKey: Any = ...
    noInputsFlag: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, center: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

SingleFrameInputCountPlugin: Any
ForcedInputCountPlugin: Any

class EvaluateLocalPhotoCalibPluginConfig(BaseMeasurementPluginConfig): ...

class EvaluateLocalPhotoCalibPlugin(GenericPlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    photoKey: Any = ...
    photoErrKey: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, center: Any) -> None: ...

class EvaluateLocalWcsPluginConfig(BaseMeasurementPluginConfig): ...

class EvaluateLocalWcsPlugin(GenericPlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    cdMatrix11Key: Any = ...
    cdMatrix12Key: Any = ...
    cdMatrix21Key: Any = ...
    cdMatrix22Key: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, center: Any) -> None: ...
    def makeLocalTransformMatrix(self, wcs: Any, center: Any): ...

class SingleFramePeakCentroidConfig(SingleFramePluginConfig): ...

class SingleFramePeakCentroidPlugin(SingleFramePlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    keyX: Any = ...
    keyY: Any = ...
    flag: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...
    @staticmethod
    def getTransformClass(): ...

class SingleFrameSkyCoordConfig(SingleFramePluginConfig): ...

class SingleFrameSkyCoordPlugin(SingleFramePlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

class ForcedPeakCentroidConfig(ForcedPluginConfig): ...

class ForcedPeakCentroidPlugin(ForcedPlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    keyX: Any = ...
    keyY: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...
    @staticmethod
    def getTransformClass(): ...

class ForcedTransformedCentroidConfig(ForcedPluginConfig): ...

class ForcedTransformedCentroidPlugin(ForcedPlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    centroidKey: Any = ...
    flagKey: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...

class ForcedTransformedShapeConfig(ForcedPluginConfig): ...

class ForcedTransformedShapePlugin(ForcedPlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    shapeKey: Any = ...
    flagKey: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...