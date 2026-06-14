import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rick_and_morty.settings")

application = get_wsgi_application()
