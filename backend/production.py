from .settings import *
from .settings import *

if os.getenv('DATABASE') == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }




    if os.getenv("POSTGRES_PATH") and os.getenv("POSTGRES_PATH") != "":
        DATABASES['default']['OPTIONS'] = {"options": f'-c search_path={os.getenv("POSTGRES_PATH")}'}

if os.getenv("ALLOWED_HOST_1") != 'None':
    ALLOWED_HOSTS.append(os.getenv("ALLOWED_HOST_1"))
if os.getenv("ALLOWED_HOST_2") != 'None':
    ALLOWED_HOSTS.append(os.getenv("ALLOWED_HOST_2"))
if os.getenv("ALLOWED_HOST_3") != 'None':
    ALLOWED_HOSTS.append(os.getenv("ALLOWED_HOST_3"))
if os.getenv("ALLOWED_HOST_4") != 'None':
    ALLOWED_HOSTS.append(os.getenv("ALLOWED_HOST_4"))
