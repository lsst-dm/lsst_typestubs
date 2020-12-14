from typing import Any

STR_PADDING: int

class SourceData:
    datasetType: Any = ...
    repoInfoList: Any = ...
    def __init__(self, datasetType: Any, sourceKeyTuple: Any) -> None: ...
    def addSourceMetrics(self, repoInfo: Any, idKeyTuple: Any, idValList: Any, sourceTableList: Any): ...
    sourceArr: Any = ...
    sourceIdDict: Any = ...
    repoArr: Any = ...
    def finalize(self) -> None: ...

class RepositoryInfo:
    keyTuple: Any = ...
    valTuple: Any = ...
    dtype: Any = ...
    name: Any = ...
    def __init__(self, keyTuple: Any, valTuple: Any, dtype: Any, name: Any) -> None: ...

class RepositoryIterator:
    def __init__(self, formatStr: Any, **dataDict: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def format(self, valDict: Any): ...
    def getKeyTuple(self): ...
