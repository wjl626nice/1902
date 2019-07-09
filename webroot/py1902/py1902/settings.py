"""
Django settings for py1902 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*!b8$5*w^zcz$m@875#i(u2!21k9zz9=$j_s4zhfbw*2ypeh+f'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发阶段 开启调试模式
DEBUG = True
# 设置允许请求的主机
ALLOWED_HOSTS = ['127.0.0.1', 'www.xuxin.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'manager.apps.ManagerConfig',
    'Home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'CheckLoginMW.CheckLoginMW'
]

ROOT_URLCONF = 'py1902.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 模板引擎初始化参数，在模板中可以直接使用。
                'conf.global.auto_config'
            ],
        },
    },
]

WSGI_APPLICATION = 'py1902.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p1_blog',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': '3306'
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# 盐
SALT = 'qwsa12#'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 媒体文件路径 别名
MEDIA_URL = '/uploads/'
# 指定媒体文件路径
# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads'),
# 后台菜单
MENU = [
    {"id": "menu-article", "title": "文章管理", "url": '#', "icon": '&#xe613;', 'child': [
        {"title": "栏目管理", "url": '/admin/category/'},
        {"title": "文章列表", "url": '/admin/article/'}
    ]
     },
    {"id": "menu-picture", "title": "随手拍管理", "url": '#', "icon": '&#xe613;', 'child': [
        {"title": "图片管理", "url": '#'},
    ]
     },
    {"id": "menu-banner", "title": "轮播图管理", "url": '#', "icon": '&#xe613;', 'child': [
        {"title": "轮播图", "url": '#'},
    ]
     },
    {"id": "menu-comments", "title": "评论管理", "url": '#', "icon": '&#xe613;', 'child': [
        {"title": "评论列表", "url": '#'}
    ]
     },
    {"id": "menu-system", "title": "系统管理", "url": '#', "icon": '&#xe613;', 'child': [
        {"title": "系统设置", "url": '#'},
        {"title": "管理员管理", "url": '/admin/manager/'},
        {"title": "友情链接管理", "url": '/admin/links/'},
        {"title": "留言管理", "url": '#'},
        {"title": "屏蔽词", "url": '#'},
        {"title": "操作日志", "url": '#'},
    ]
     },
]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# 极验id和key
GEETEST = {
    'id': '4726b9849ea9f2493787a3fa247a9973',
    'key': 'c264c310dbae53a1383770771408b473',
}