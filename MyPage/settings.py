import os
import sys

# base content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'uvwctn3l^-gci+r5(hq58d3f!@@9#6_vvqt9)x(fqg_8t-1_jw'

DEBUG = False

ALLOWED_HOSTS = ['*']

# App register
INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'homepage',
    'mdeditor',
    'pure_pagination',
]

# middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyPage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'blog.views.global_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyPage.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_mypage',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1'
    }
}

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件配置
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

# 网站的基本信息配置
SITE_NAME = 'BestNico'  # 站点名称
SITE_DESCRIPTION = 'BestNico'  # 站点描述
SITE_KEYWORDS = 'BestNico,Python,机器学习,极客'  # 站点关键词
SITE_TITLE = 'BestNico | Blog'  # 博客标题
SITE_TYPE_CHINESE = '有没有那么一个世界，永远不天黑'  # 打字效果 中文内容
SITE_TYPE_ENGLISH = 'The stars, sun and every object obey my wishes'  # 打字效果 英文内容
SITE_MAIL = 'Lzmkxumgh@gmail.com'  # 我的邮箱
SITE_ICP = '辽ICP备20004043号 '  # 网站备案号
SITE_ICP_URL = 'http://beian.miit.gov.cn'  # 备案号超链接地址

# 后台MarkDown编辑器配置
X_FRAME_OPTIONS = 'SAMEORIGIN'

# 日志记录
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' :"[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' :"%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'blog': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}