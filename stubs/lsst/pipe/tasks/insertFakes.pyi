from lsst.pipe.base import CmdLineTask, PipelineTask, PipelineTaskConfig, PipelineTaskConnections
from typing import Any

class InsertFakesConnections(PipelineTaskConnections):
    image: Any = ...
    fakeCat: Any = ...
    imageWithFakes: Any = ...

class InsertFakesConfig(PipelineTaskConfig):
    raColName: Any = ...
    decColName: Any = ...
    doCleanCat: Any = ...
    diskHLR: Any = ...
    bulgeHLR: Any = ...
    magVar: Any = ...
    nDisk: Any = ...
    nBulge: Any = ...
    aDisk: Any = ...
    aBulge: Any = ...
    bDisk: Any = ...
    bBulge: Any = ...
    paDisk: Any = ...
    paBulge: Any = ...
    sourceType: Any = ...
    fakeType: Any = ...
    calibFluxRadius: Any = ...
    coaddName: Any = ...
    doSubSelectSources: Any = ...
    sourceSelectionColName: Any = ...
    insertImages: Any = ...
    doProcessAllDataIds: Any = ...

class InsertFakesTask(PipelineTask, CmdLineTask):
    ConfigClass: Any = ...
    fakeSourceCatType: str = ...
    def runDataRef(self, dataRef: Any) -> None: ...
    def runQuantum(self, butlerQC: Any, inputRefs: Any, outputRefs: Any) -> None: ...
    bitmask: Any = ...
    def run(self, fakeCat: Any, image: Any, wcs: Any, photoCalib: Any): ...
    def processImagesForInsertion(self, fakeCat: Any, wcs: Any, psf: Any, photoCalib: Any, band: Any, pixelScale: Any): ...
    def addPixCoords(self, fakeCat: Any, wcs: Any): ...
    def trimFakeCat(self, fakeCat: Any, image: Any, wcs: Any): ...
    def mkFakeGalsimGalaxies(self, fakeCat: Any, band: Any, photoCalib: Any, pixelScale: Any, psf: Any, image: Any) -> None: ...
    def mkFakeStars(self, fakeCat: Any, band: Any, photoCalib: Any, psf: Any, image: Any) -> None: ...
    def cleanCat(self, fakeCat: Any, starCheckVal: Any): ...
    def addFakeSources(self, image: Any, fakeImages: Any, sourceType: Any): ...
