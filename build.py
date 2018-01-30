from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("python.sphinx")


description = "I am trying to learn Python"
license = 'GNU GPL v3'
version = '0.0.1'
name = "mentoring"
default_task = ['clean', 'analyze', 'publish']

#default_task = "publish"


@init
def set_properties(project):
    project.set_property('coverage_exceptions', ['run',])
    project.set_property('coverage_branch_threshold_warn', 70)
    project.set_property('coverage_branch_partial_threshold_warn', 70)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('sphinx_builder', 'html')
