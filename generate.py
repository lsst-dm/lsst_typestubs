#!/usr/bin/env python

import eups
import subprocess
import os

for name, version, _, _ in eups.getDependencies('lsst_distrib', topological=True):
    dir = eups.productDir(name, versionName=version)
    if os.path.exists(f"{dir}/python"):
        output = subprocess.run(["stubgen", "-o", "stubs", f"{dir}/python"], capture_output=True)
