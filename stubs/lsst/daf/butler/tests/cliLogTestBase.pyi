from lsst.daf.butler.cli.cliLog import CliLog as CliLog
from lsst.daf.butler.cli.utils import LogCliRunner as LogCliRunner, clickResultMsg as clickResultMsg, command_test_env as command_test_env
from typing import Any

def hasLsstLogHandler(logger: Any): ...
def command_log_settings_test(expected_pyroot_level: Any, expected_pybutler_level: Any, expected_lsstroot_level: Any, expected_lsstbutler_level: Any) -> None: ...

class CliLogTestBase:
    lsstLogHandlerId: Any = ...
    runner: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    class PythonLogger:
        logger: Any = ...
        initialLevel: Any = ...
        def __init__(self, component: Any) -> None: ...
    class LsstLogger:
        logger: Any = ...
        initialLevel: Any = ...
        def __init__(self, component: Any) -> None: ...
    def runTest(self, cmd: Any) -> None: ...
    def test_butlerCliLog(self) -> None: ...
    def test_helpLogReset(self) -> None: ...
    def testLongLog(self) -> None: ...
