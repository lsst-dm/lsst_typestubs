import lsst.pex.exceptions
from lsst.ap.verify.config import Config as Config

class DataTestCase(lsst.utils.tests.TestCase):
    testDataset: str = ...
    datasetKey: str = ...
    @classmethod
    def setUpClass(cls) -> None: ...