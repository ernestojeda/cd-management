
# Copyright (c) 2020 Intel Corporation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pybuilder.core import use_plugin
from pybuilder.core import init
from pybuilder.core import Author

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_anybadge')
use_plugin('python.install_dependencies')

name = 'badger'
authors = [Author('Ernesto Ojeda', 'ernesto.ojeda@intel.com')]
summary = 'A Python script finds GitHub contributors and gives them badges'
url = 'https://github.com/edgexfoundry/cd-management/tree/badger'
version = '0.0.1'
default_task = [
    'clean',
    'analyze',
    'radon',
    'bandit',
    'anybadge',
    'package']


@init
def set_properties(project):
    project.set_property('unittest_module_glob', 'test_*.py')
    project.set_property('coverage_break_build', False)
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_ignore', 'E501, W503, F401, E722, W605')
    project.build_depends_on_requirements('requirements-build.txt')
    project.depends_on_requirements('requirements.txt')
    project.set_property('distutils_console_scripts',
                         ['badger = badger.cli:main'])
    project.set_property('radon_break_build_average_complexity_threshold', 5)
    project.set_property('radon_break_build_complexity_threshold', 17)
    project.set_property('bandit_break_build', True)
    project.set_property('anybadge_add_to_readme', True)
    project.set_property('anybadge_complexity_use_average', True)
    project.set_property('anybadge_use_shields', True)
