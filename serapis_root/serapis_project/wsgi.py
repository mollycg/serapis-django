import os
import sys

from django.core.wsgi import get_wsgi_application

path = os.path.expanduser('~/serapis_project')

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'serapis_project.settings'


application = get_wsgi_application()