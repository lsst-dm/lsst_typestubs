from typing import Any

class AllocatorParser:
    defaults: Any = ...
    args: Any = ...
    def __init__(self, basename: Any) -> None: ...
    def parseArgs(self, basename: Any): ...
    def getArgs(self): ...
    def getPlatform(self): ...