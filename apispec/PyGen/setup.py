#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name="pygen",
    version="1.0.0",
    author="Wen Li",
    author_email="li.wen@wsu.edu",
    description="python APP generation",
    long_description_content_type="text/markdown",
    url="https://github.com/Daybreak2019/CpyFuzz",
    packages=['pygen'],
    install_requires=['progressbar', 'astunparse']
)
