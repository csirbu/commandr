# Copyright 2013 TellApart, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    'command',
    'Run',
    'SetOptions',
    'Usage',
    'update_wrapper',
    'wraps',
    'MonkeyPatchFunctools',
    'CommandrError',
    'CommandrUsageError',
    'CommandrDuplicateMainError']

# Export the global Commandr object methods.
from commandr.commandr import Commandr
from commandr.commandr import CommandrError
from commandr.commandr import CommandrUsageError
from commandr.commandr import CommandrDuplicateMainError

_COMMANDR = Commandr()

command = _COMMANDR.command
Run = _COMMANDR.Run
RunFunction = _COMMANDR.RunFunction
SetOptions = _COMMANDR.SetOptions
Usage = _COMMANDR.Usage

# Export the decorator utils.
from commandr.functools_util import update_wrapper, wraps, MonkeyPatchFunctools
