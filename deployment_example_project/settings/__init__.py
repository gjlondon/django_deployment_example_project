# application_python cookbook expects manage.py in a top level
# instead of app level dir, so the relative import can fail
try:
    from .deployment_example_project.deployment_example_project.settings.base import *
except ImportError:
    from deployment_example_project.settings.base import *


try:
    from local_settings import *
except ImportError:
    pass
