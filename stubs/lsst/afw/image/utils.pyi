from typing import Any

def clipImage(im: Any, minClip: Any, maxClip: Any) -> None: ...
def resetFilters() -> None: ...
def defineFilter(name: Any, lambdaEff: Any, lambdaMin: Any = ..., lambdaMax: Any = ..., alias: Any = ..., force: bool = ...) -> None: ...
def getProjectionIndices(imageBBox: Any, targetBBox: Any): ...
def projectImage(image: Any, bbox: Any, fill: int = ...): ...