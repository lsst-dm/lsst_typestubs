from typing import Any

class WcsFactory:
    def __init__(self, pixelScale: Any, projection: Any, rotation: Any = ..., flipX: bool = ...) -> None: ...
    def makeWcs(self, crPixPos: Any, crValCoord: Any): ...
