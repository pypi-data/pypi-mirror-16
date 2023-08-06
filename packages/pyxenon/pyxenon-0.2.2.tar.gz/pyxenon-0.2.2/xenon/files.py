# PyXenon Xenon API wrapper
#
# Copyright 2015 Netherlands eScience Center
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

'''
Classes and enums in files.

To use as arguments in API calls. The `package` variable stores the Java
package name of the Xenon files API.
'''

from .java import nl

package = 'nl.esciencecenter.xenon.files'
__all__ = ['RelativePath', 'OpenOption', 'CopyOption', 'PosixFilePermission']

RelativePath = None
PosixFilePermission = None
OpenOption = None
CopyOption = None


def _init():
    ''' Initialize classes. Only to be called in xenon.init. '''
    global RelativePath, PosixFilePermission, OpenOption, CopyOption

    RelativePath = nl.esciencecenter.xenon.files.RelativePath
    PosixFilePermission = nl.esciencecenter.xenon.files.PosixFilePermission
    OpenOption = nl.esciencecenter.xenon.files.OpenOption
    CopyOption = nl.esciencecenter.xenon.files.CopyOption
