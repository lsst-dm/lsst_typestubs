from typing import Any

class FsScanner:
    globString: Any = ...
    fields: Any = ...
    reString: str = ...
    def __init__(self, pathTemplate: Any) -> None: ...
    def getFields(self): ...
    def isNumeric(self, name: Any): ...
    def isInt(self, name: Any): ...
    def isFloat(self, name: Any): ...
    def processPath(self, location: Any): ...