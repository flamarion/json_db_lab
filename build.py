from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = "mentoring"
default_task = "publish"


@init
def set_properties(project):
    project.set_property_if_unset("coverage_threshold_warn", 95)
