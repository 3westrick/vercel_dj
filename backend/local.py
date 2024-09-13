from .settings import *

if os.getenv('DATABASE') == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('postgres'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }

    if os.getenv("POSTGRES_PATH"):
        DATABASES['default']['OPTIONS'] = {"options": f'-c search_path={os.getenv("POSTGRES_PATH")}'}

