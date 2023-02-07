# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Two-level fuzzing for python interpreter and runtime libraries"""


import sys
from .import_hook import instrument_imports

def _InstrumentAll ():
    with instrument_imports():
        import quopri


def _SetupPyGen ():
    pass

def SetupPyFuzz ():
    # 1. setup the python app generator
    _SetupPyGen ()

    # 2. instrument all python runtimes
    _InstrumentAll ()


def PyMutation ():
    pass
    

