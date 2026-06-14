import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rick_and_morty.settings")

application = get_asgi_application()
