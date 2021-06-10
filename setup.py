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

from __future__ import absolute_import

from setuptools import find_packages
from setuptools import setup

version = "1.0.2"

setup(
    name="kt-legacy",
    version=version,
    description="Legacy import names for Keras Tuner",
    url="https://github.com/haifeng-jin/kt-legacy",
    author="Haifeng Jin",
    license="Apache License 2.0",
    packages=find_packages(),
)
