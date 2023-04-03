from fuzzwrap import Calibrate
from platform import python_version

py_version = python_version()


SeedPath = f'../experiments/seeds_python{py_version}'
Calibrate (SeedPath)