from typing import Any, Optional

class Bcolors:
    HEADER: str = ...
    OKBLUE: str = ...
    OKGREEN: str = ...
    WARNING: str = ...
    FAIL: str = ...
    ENDC: str = ...
    BOLD: str = ...
    UNDERLINE: str = ...

def run(repo_or_json: Any, outputPrefix: Optional[Any] = ..., makePrint: bool = ..., makePlot: bool = ..., level: str = ..., metrics_package: str = ..., **kwargs: Any) -> None: ...
def runOneFilter(repo: Any, visitDataIds: Any, brightSnrMin: Optional[Any] = ..., brightSnrMax: Optional[Any] = ..., makeJson: bool = ..., filterName: Optional[Any] = ..., outputPrefix: str = ..., doApplyExternalPhotoCalib: bool = ..., externalPhotoCalibName: Optional[Any] = ..., doApplyExternalSkyWcs: bool = ..., externalSkyWcsName: Optional[Any] = ..., skipTEx: bool = ..., verbose: bool = ..., metrics_package: str = ..., instrument: str = ..., dataset_repo_url: str = ..., skipNonSrd: bool = ..., **kwargs: Any): ...
def plot_metrics(job: Any, filterName: Any, outputPrefix: str = ...) -> None: ...
def print_metrics(job: Any, levels: Any = ...) -> None: ...
def print_pass_fail_summary(jobs: Any, levels: Any = ..., default_level: str = ...) -> None: ...