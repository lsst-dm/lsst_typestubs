from .. import opt as opt, script as script
from lsst.daf.butler.cli.utils import MWCommand as MWCommand, cli_handle_exception as cli_handle_exception
from typing import Any

class BpsCommand(MWCommand):
    extra_epilog: str = ...

def transform(*args: Any, **kwargs: Any) -> None: ...
def prepare(*args: Any, **kwargs: Any) -> None: ...
def submit(*args: Any, **kwargs: Any) -> None: ...
def report(*args: Any, **kwargs: Any) -> None: ...
