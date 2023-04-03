
from setuptools import setup
from setuptools import find_packages


setup(
    name="fuzzwrap",
    version="0.0.1",
    author="Wen Li",
    author_email="li.wen@wsu.edu",
    description="fuzz wrapping",
    url="https://github.com/Daybreak2019/CpyFuzz",
    packages=['fuzzwrap'],
    install_requires=['psutil']
)
