from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from environs import Env

#Envoriments var
env = Env()
env.read_env()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY") #django-insecure-+wtr%x#gjqd7uqs_jy#(1sq*d-h1ff7h#fsu^9n^iu+^^ufhqq

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'users.apps.UsersConfig',
    'BlogAPI', #API

    #pip installed apps
    'crispy_forms', #pip install  django-crispy-forms  bu css bilan ishlash kerak buladi
    'widget_tweaks', #pip install django-widget-tweak
    'ckeditor_uploader', #pip install django-ckeditor
    'social_django',    #pip install social-auth-app-django
    #Api
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders', #pip install django-cors-headers
    'dj_rest_auth',#pip install dj-rest-auth
    'drf_yasg', #pip install drf-yasg
    
] 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware', #social media
]

#qaysilari uchun mumkin
CORS_ORIGIN_WHITELIST = (
    "http://127.0.0.1:8000",
    "http://localhost:3000",#react uchun
)

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #social facebook
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

#Social media
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =[
    BASE_DIR / 'static/'
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

#####################################################################################################

MEDIA_ROOT = os.path.join(BASE_DIR,'media') #rasm faylarni saqlash uchun
MEDIA_URL = '/media/'

########################################################################### pip install  django-crispy-forms

CRISPY_TEMPLATE_PACK = 'bootstrap4'

######################################################################################################
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login' 
LOGOUT_URL = 'logout'

# EMAIL reset

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'xackercoder@gmail.com'
EMAIL_HOST_PASSWORD = "kaiycghaxwdgisfy"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#restAPI
REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# CKEDITOR
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'Full',
    },
}
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True


#login with social media
SOCIAL_AUTH_FACEBOOK_KEY = '546795753316726'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'ced824ffb80027ebd4e7252949f264ea'  # App Secret

