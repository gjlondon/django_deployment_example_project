import os
import sys

# application_python cookbook expects manage.py in a top level
# instead of app level dir, so the relative import can fail
try:
    from .deployment_example_project.deployment_example_project.settings.base import *
except ImportError:
    from deployment_example_project.settings.base import *


try:
    # add the /shared directory so that migrate can run
    # before the /release directories are symlinked
    #sys.path.append(sys.path[0].rsplit("/", 1)[0])
    from local_settings import *
except ImportError:
    print "import error"
    pass
