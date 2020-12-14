from lsst.daf.base import PropertyList as PropertyList
from lsst.obs.base import createInitialSkyWcs as createInitialSkyWcs
from typing import Any, Optional

def makeConfigDict(config: Any, log: Any, camera: Any, maxIter: Any, resetFitParameters: Any, outputZeropoints: Any, tract: Optional[Any] = ...): ...
def translateFgcmLut(lutCat: Any, filterMap: Any): ...
def translateVisitCatalog(visitCat: Any): ...
def computeCcdOffsets(camera: Any, defaultOrientation: Any): ...
def computeReferencePixelScale(camera: Any): ...
def computeApproxPixelAreaFields(camera: Any): ...
def makeZptSchema(superStarChebyshevSize: Any, zptChebyshevSize: Any): ...
def makeZptCat(zptSchema: Any, zpStruct: Any): ...
def makeAtmSchema(): ...
def makeAtmCat(atmSchema: Any, atmStruct: Any): ...
def makeStdSchema(nBands: Any): ...
def makeStdCat(stdSchema: Any, stdStruct: Any, goodBands: Any): ...
def computeApertureRadiusFromDataRef(dataRef: Any, fluxField: Any): ...
def computeApertureRadiusFromName(fluxField: Any): ...
def extractReferenceMags(refStars: Any, bands: Any, filterMap: Any): ...
