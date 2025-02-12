
import os
import dotenv

from django.core.wsgi import get_wsgi_application


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

application = get_wsgi_application()
