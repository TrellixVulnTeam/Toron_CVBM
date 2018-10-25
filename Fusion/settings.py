

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=&w9due426k@l^ju1=s1)fj1rnpf0ok8xvjwx+62_nc-f12-8('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Google authentication
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'hd': 'iiitdmj.ac.in',
        }
    }
}

# allauth settings

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/dashboard'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'

# email of sender
# TODO: Remove Ramlal!
EMAIL_HOST_USER = 'ramlalfff@gmail.com'

# password of sender
EMAIL_HOST_PASSWORD = ''

EMAIL_PORT = 587
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/accounts/login/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Fusion: '
DEFAULT_FROM_EMAIL = 'ramlalfff@gmail.com'

SERVER_EMAIL = 'ramlalfff@gmail.com'

ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_USERNAME_MIN_LENGTH = 3

SOCIALACCOUNT_ADAPTER = 'applications.globals.adapters.MySocialAccountAdapter'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'applications.academic_procedures.apps.AcademicProceduresConfig',
    'applications.academic_information.apps.AcademicInformationConfig',
    'applications.central_mess.apps.CentralMessConfig',
    'applications.complaint_system.apps.ComplaintSystemConfig',
    'applications.file_tracking.apps.FileTrackingConfig',
    'applications.finance_accounts.apps.FinanceAccountsConfig',
    'applications.gymkhana.apps.GymkhanaConfig',
    'applications.globals.apps.GlobalsConfig',
    'applications.health_center.apps.HealthCenterConfig',
    'applications.leave.apps.LeaveConfig',    'applications.online_cms.apps.OnlineCmsConfig',
    'applications.placement_cell.apps.PlacementCellConfig',
    'applications.scholarships.apps.ScholarshipsConfig',
    'applications.visitor_hostel.apps.VisitorHostelConfig',
    'applications.eis.apps.EisConfig',
    'allauth.account',
    'allauth.socialaccount',
    'allauth',
    'allauth.socialaccount.providers.google',
    'semanticuiforms',
    'applications.feeds.apps.FeedsConfig',
    'pagedown',
    'markdown_deux',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Fusion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/', os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Fusion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

