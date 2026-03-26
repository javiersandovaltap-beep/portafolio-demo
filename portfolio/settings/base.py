from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cv',  # Tu app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # <- OBLIGATORIO Y PRIMERO
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <- DEBE IR DESPUÉS DE SESSIONS
    'django.contrib.messages.middleware.MessageMiddleware', # <- OBLIGATORIO
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'
WSGI_APPLICATION = 'portfolio.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'cv/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# Asegúrate de que DEBUG esté en True para desarrollo local
DEBUG = True

# Puedes dejar ALLOWED_HOSTS vacío cuando DEBUG es True, 
# pero si quieres puedes agregar tu host local por si acaso:
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # ← Esta línea es la que falta
# STATICFILES_DIRS = [BASE_DIR / 'static']

# SEGURIDAD: Clave secreta obligatoria de Django (puedes inventar cualquier texto largo aquí)
SECRET_KEY = os.environ.get('SECRET_KEY')


# Configuración de la base de datos por defecto (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Tipo de campo automático por defecto para los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REDIRECCIONES DE LOGIN/LOGOUT
LOGIN_REDIRECT_URL = 'inicio'   # A dónde ir si el login es exitoso
LOGIN_URL = 'login'             # A dónde ir si alguien sin sesión intenta entrar a una URL protegida
LOGOUT_REDIRECT_URL = 'inicio'  # A dónde ir después de cerrar sesión
