"""
Django settings for test01 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# 项目根目录
# __file__ 文件的路径
# os.path.abspath 获取文件的绝对路径
# os.path.dirname 获取文件所在的目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = /Users/qingyun/1902/python/Django/20190523/test01

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wv+64-c5u)4iyx)v3jl*ix&3j=gu1+*&)djfido(7^nus$l21n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 路由  uri 和函数对应的模块
ROOT_URLCONF = 'test01.urls'

# 设置模板配置
TEMPLATES = [
    {
        # 模板引擎，jinja2
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置模板的位置  os.path.join  可以让咱们写的程序跨平台，不同操作系统目录分隔符不一样。
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        # window 目录：C:\\abc\\ab\\aa
        # linux  目录：/abc/ab/aa
        # os.path.join(BASE_DIR, 'templates') 结果：/Users/qingyun/1902/python/Django/20190523/test01/templates
        ,
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

WSGI_APPLICATION = 'test01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# 设置中国的时区   PRC 中华人民共和国
TIME_ZONE = 'PRC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# css js  image等静态文件保存的路径 别名。相当于STATICFILES_DIRS的别名
STATIC_URL = '/static/'
# Django项目中所有的css js image 都会从该配置目录中查找对应文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]