from .opt import delete_option as delete_option, task_option as task_option
from collections import namedtuple
from lsst.daf.butler.cli.opt import config_file_option as config_file_option, config_option as config_option
from lsst.daf.butler.cli.utils import MWCommand as MWCommand
from lsst.obs.base.cli.opt import instrument_option as instrument_option
from typing import Any

_PipelineAction = namedtuple('_PipelineAction', 'action,label,value')

class _PipelineActionType:
    action: Any = ...
    regex: Any = ...
    valueType: Any = ...
    def __init__(self, action: Any, regex: str = ..., valueType: Any = ...) -> None: ...
    def __call__(self, value: Any): ...

def makePipelineActions(args: Any, taskFlags: Any = ..., deleteFlags: Any = ..., configFlags: Any = ..., configFileFlags: Any = ..., instrumentFlags: Any = ...): ...

class PipetaskCommand(MWCommand):
    extra_epilog: str = ...
