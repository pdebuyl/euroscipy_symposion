import os
import sys
sys.path.append("/home/pierre/ve-django-5/euroscipy_symposion")

activate_this = '/home/pierre/ve-django-5/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "symposion_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
