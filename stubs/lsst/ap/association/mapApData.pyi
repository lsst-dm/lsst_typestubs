import lsst.pex.config as pexConfig
import lsst.pex.config as pipeBase
from typing import Any, Optional

class MapApDataConfig(pexConfig.Config):
    copyColumns: Any = ...

class MapApDataTask(pipeBase.Task):
    ConfigClass: Any = ...
    inputSchema: Any = ...
    outputSchema: Any = ...
    mapper: Any = ...
    def __init__(self, inputSchema: Any, outputSchema: Any, **kwargs: Any) -> None: ...
    def run(self, inputCatalog: Any, exposure: Optional[Any] = ...): ...

class MapDiaSourceConfig(pexConfig.Config):
    copyColumns: Any = ...
    calibrateColumns: Any = ...
    flagMap: Any = ...
    dipFluxPrefix: Any = ...
    dipSepColumn: Any = ...

class MapDiaSourceTask(MapApDataTask):
    ConfigClass: Any = ...
    def __init__(self, inputSchema: Any, **kwargs: Any) -> None: ...
    def run(self, inputCatalog: Any, exposure: Any, return_pandas: bool = ...): ...
    def calibrateFluxes(self, inputRecord: Any, outputRecord: Any, photoCalib: Any) -> None: ...
    def computeDipoleFluxes(self, inputRecord: Any, outputRecord: Any, photoCalib: Any) -> None: ...
    def computeDipoleSep(self, inputRecord: Any, outputRecord: Any, wcs: Any) -> None: ...
    def bitPackFlags(self, inputRecord: Any, outputRecord: Any) -> None: ...
    def computeBBoxSize(self, inputRecord: Any, outputRecord: Any) -> None: ...

class UnpackApdbFlags:
    bit_pack_columns: Any = ...
    output_flag_columns: Any = ...
    def __init__(self, flag_map_file: Any, table_name: Any) -> None: ...
    def unpack(self, input_flag_values: Any, flag_name: Any): ...
