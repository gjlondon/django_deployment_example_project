import os
import sys

from .deployment_example_project.deployment_example_project.settings.base import *

execfile("../../project.settings")
name = os.getenv("PROJECT_NAME")

try:
    sys.path.append("/srv/{name}/shared".format(name=name))
    from local_settings import *
except ImportError:
    pass
