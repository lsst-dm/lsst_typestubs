from typing import Any

def getVersionFromPythonModule(module: Any): ...
def getPythonPackages(): ...
def getEnvironmentPackages(): ...
def getCondaPackages(): ...

class Packages:
    formats: Any = ...
    def __init__(self, packages: Any) -> None: ...
    @classmethod
    def fromSystem(cls): ...
    @classmethod
    def fromBytes(cls, data: Any, format: Any): ...
    @classmethod
    def read(cls, filename: Any): ...
    def toBytes(self, format: Any): ...
    def write(self, filename: Any) -> None: ...
    def __len__(self): ...
    def __contains__(self, pkg: Any): ...
    def __iter__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def update(self, other: Any) -> None: ...
    def extra(self, other: Any): ...
    def missing(self, other: Any): ...
    def difference(self, other: Any): ...
