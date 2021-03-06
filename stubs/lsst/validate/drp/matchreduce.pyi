from typing import Any, Optional

def build_matched_dataset(repo: Any, dataIds: Any, matchRadius: Optional[Any] = ..., brightSnrMin: Optional[Any] = ..., brightSnrMax: Optional[Any] = ..., faintSnrMin: Optional[Any] = ..., faintSnrMax: Optional[Any] = ..., doApplyExternalPhotoCalib: bool = ..., externalPhotoCalibName: Optional[Any] = ..., doApplyExternalSkyWcs: bool = ..., externalSkyWcsName: Optional[Any] = ..., skipTEx: bool = ..., skipNonSrd: bool = ...): ...
def getKeysFilter(schema: Any, nameFluxKey: Optional[Any] = ...): ...
def filterSources(allMatches: Any, keys: Optional[Any] = ..., faintSnrMin: Optional[Any] = ..., brightSnrMin: Optional[Any] = ..., safeExtendedness: Optional[Any] = ..., extended: bool = ..., faintSnrMax: Optional[Any] = ..., brightSnrMax: Optional[Any] = ...): ...
def summarizeSources(blob: Any, filterResult: Any) -> None: ...
