from ._butlerUri import ButlerURI
from typing import Optional, Union

BUTLER_ROOT_TAG: str

def replaceRoot(configRoot: str, butlerRoot: Optional[Union[ButlerURI, str]]) -> str: ...
