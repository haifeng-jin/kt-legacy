# Copyright 2019 The Keras Tuner Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script."""

from setuptools import setup
from setuptools import find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

__version__ = "1.0.5"
setup(
    name="kt-legacy",
    version=__version__,
    description="Legacy import names for KerasTuner",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/haifeng-jin/kt-legacy",
    author="Haifeng Jin",
    license="Apache License 2.0",
    packages=find_packages(),
)