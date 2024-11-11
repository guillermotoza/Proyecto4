"""
Django settings for sayl project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c^hv-3u74aino8lad5@_36t=%96w6b7za9_df)$0y3=t!wn#$r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'app_tipojustificacion.apps.AppTipoJustificacionConfig',
    'app_horarios.apps.AppHorariosConfig',
    'app_justificacion.apps.AppJustificacionConfig',
    'auditoria.apps.AuditoriaConfig',
    'calendario.apps.CalendarioConfig',
    'asistencias.apps.AsistenciasConfig',
    'edificios.apps.EdificiosConfig',
    'mensajeria.apps.MensajeriaConfig',
    'cargos.apps.CargosConfig',
    'estadisticas.apps.EstadisticasConfig',
    'config.apps.ConfigConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'login.apps.LoginConfig',
    'rest_framework',
    'reversion',
    'simple_history',
    'background_task',
    'django_crontab',
    
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'sayl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "sayl","templates"),
            os.path.join(BASE_DIR, "app_horarios","templates"),
            os.path.join(BASE_DIR, "app_tipojustificacion","templates"),
            os.path.join(BASE_DIR, "app_justificacion","templates"),
            os.path.join(BASE_DIR, "login","templates"),
            os.path.join(BASE_DIR, "asistencias","templates"),
            os.path.join(BASE_DIR, "edificios","templates"),
            os.path.join(BASE_DIR, "mensajeria","templates"),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'sayl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'login.CustomUser'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'sayl', 'static'),)

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


#Para d esactivar la debug toolbar
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'

# # Para simular mandar correos. Los "correos" se guardan en la carpeta sent_emails
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


#Configuracion para correo gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'supervisoraylunam@gmail.com'
EMAIL_HOST_PASSWORD = 'supervisor1234'

#Lugar donde se guardan las imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 
MEDIA_URL = '/media/'

#Aca se dicen cuando y que se va a ejecutar en el cron. (Tareas Automaticas)
#Se usa el formato de crontab de unix para establecer el cuando 
#(https://www.redeszone.net/2017/01/09/utilizar-cron-crontab-linux-programar-tareas/)
#(https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/)

CRONJOBS = [
    ('* * * * *', 'asistencias.cron.asignar_inasistencia', '>> /home/bjar/Documents/scheduled_job.log')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'