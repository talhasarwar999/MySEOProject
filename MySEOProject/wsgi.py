
import os
import sys
sys.path.append('/opt/bitnami/projects/MySEOProject')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/MySEOProject/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySEOProject.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
