from os import path
import sys

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

sys.path.insert(0, path.join(PROJECT_ROOT, "../../motor/"))
sys.path.insert(1, path.join(PROJECT_ROOT, "apps/"))

try:
    from YBAQNEXT.settings import *
    from YBWEB.ctxJSON import DICTJSON
except ImportError as exc:
    print(exc)


YEBO_APPS = ('models', )

rest = open(path.join(PROJECT_ROOT, "config/urls.json")).read()
oRest = DICTJSON.fromJSON(rest)

for app in oRest:
    YEBO_APPS += (app, )

INSTALLED_APPS += YEBO_APPS

try:
    from .local import *
except ImportError:
    pass
