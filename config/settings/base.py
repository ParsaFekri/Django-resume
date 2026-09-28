from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 'django-insecure-37e3wka_$!7#e43otb646d50i_^rcuu9n*p(6+0++_m_*h50ko'
SECRET_KEY = config('SECRET_KEY') 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # myapp
    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
    'portfolio.apps.PoertfolioConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # mymiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  #
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# ========== زبان و زمان ==========
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# ========== تنظیمات فایل‌های استاتیک و مدیا (رسانه) ==========
# فایل‌های استاتیک شامل CSS، جاوااسکریپت، تصاویر ثابت و ... هستند که در توسعه توسط جنگو سرو می‌شوند
STATIC_URL = 'static/'  # آدرس پیشوندی که فایل‌های استاتیک از طریق آن درخواست می‌شوند (مثلاً /static/style.css)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # مسیر پوشه‌ای که فایل‌های استاتیک پروژه در آن قرار دارند (معمولاً کنار manage.py)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# فایل‌های مدیا شامل فایل‌های آپلودی کاربران (تصاویر پروفایل، فایل‌های ضمیمه و ...) هستند
MEDIA_URL = '/media/'  # آدرس پیشوندی برای دسترسی به فایل‌های مدیا (مثلاً /media/profile_pics/avatar.jpg)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # مسیر فیزیکی ذخیره‌سازی فایل‌های مدیا روی دیسک (در ریشه پروژه)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'