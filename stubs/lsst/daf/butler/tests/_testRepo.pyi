from typing import Any, Optional

def makeTestRepo(root: Any, dataIds: Any, *, config: Optional[Any] = ..., **kwargs: Any): ...
def makeTestCollection(repo: Any): ...
def expandUniqueId(butler: Any, partialId: Any): ...
def addDatasetType(butler: Any, name: Any, dimensions: Any, storageClass: Any): ...

class DatastoreMock:
    @staticmethod
    def apply(butler: Any) -> None: ...
