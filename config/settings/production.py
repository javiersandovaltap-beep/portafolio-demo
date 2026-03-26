import dj_database_url
import os
from .base import *

DEBUG = False

# Lee la URL de tu archivo .env
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}
