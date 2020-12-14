import click.testing
from ..core.config import Config as Config
from ..core.utils import iterable as iterable
from .cliLog import CliLog as CliLog
from typing import Any, Optional

log: Any
mockEnvVarKey: str
mockEnvVar: Any
typeStrAcceptsMultiple: str
typeStrAcceptsSingle: str
split_kv_separator: str

def textTypeStr(multiple: Any): ...

class Mocker:
    mock: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def reset(cls) -> None: ...

class LogCliRunner(click.testing.CliRunner):
    def invoke(self, *args: Any, **kwargs: Any): ...

def clickResultMsg(result: Any): ...
def command_test_env(runner: Any, commandModule: Any, commandName: Any) -> None: ...
def addArgumentHelp(doc: Any, helpText: Any): ...
def split_commas(context: Any, param: Any, values: Any): ...
def split_kv(context: Any, param: Any, values: Any, choice: Optional[Any] = ..., multiple: bool = ..., normalize: bool = ..., separator: str = ..., unseparated_okay: bool = ..., return_type: Any = ..., default_key: str = ..., reverse_kv: bool = ..., add_to_default: bool = ...): ...
def to_upper(context: Any, param: Any, value: Any): ...
def unwrap(val: Any): ...
def cli_handle_exception(func: Any, *args: Any, **kwargs: Any): ...

class option_section:
    sectionText: Any = ...
    def __init__(self, sectionText: Any) -> None: ...
    def __call__(self, f: Any): ...

class MWPath(click.Path):
    mustNotExist: Any = ...
    def __init__(self, exists: Optional[Any] = ..., file_okay: bool = ..., dir_okay: bool = ..., writable: bool = ..., readable: bool = ..., resolve_path: bool = ..., allow_dash: bool = ..., path_type: Optional[Any] = ...) -> None: ...
    def convert(self, value: Any, param: Any, ctx: Any): ...

class MWOption(click.Option):
    def make_metavar(self): ...

class MWArgument(click.Argument):
    def make_metavar(self): ...

class OptionSection(MWOption):
    @property
    def hidden(self): ...
    @hidden.setter
    def hidden(self, val: Any) -> None: ...
    sectionText: Any = ...
    def __init__(self, sectionName: Any, sectionText: Any) -> None: ...
    def get_help_record(self, ctx: Any): ...

class MWOptionDecorator:
    partialOpt: Any = ...
    def __init__(self, *param_decls: Any, **kwargs: Any) -> None: ...
    def name(self): ...
    def opts(self): ...
    @property
    def help(self): ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class MWArgumentDecorator:
    partialArg: Any = ...
    def __init__(self, *param_decls: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, help: Optional[Any] = ..., **kwargs: Any): ...

class MWCommand(click.Command):
    extra_epilog: Any = ...
    def parse_args(self, ctx: Any, args: Any) -> None: ...
    @property
    def epilog(self): ...
    @epilog.setter
    def epilog(self, val: Any) -> None: ...

class ButlerCommand(MWCommand):
    extra_epilog: str = ...

class MWCtxObj:
    args: Any = ...
    def __init__(self) -> None: ...
    @staticmethod
    def getFrom(ctx: Any): ...

def yaml_presets(ctx: Any, param: Any, value: Any) -> None: ...
def sortAstropyTable(table: Any, dimensions: Any, sort_first: Optional[Any] = ...): ...