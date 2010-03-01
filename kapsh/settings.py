import os

from settings_kapsh.settings_local import *

PROJECT_ROOT = os.path.dirname(__file__)

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'kapsh.urls'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "kapsh.tweets.context_processors.twitter_user",
    "kapsh.comments.context_processors.intense_debate_acct",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'kapsh.authors',
    'kapsh.blog',
    'kapsh.categories',
    'kapsh.content',
    'kapsh.flickr',
    'kapsh.tweets',
    'tagging',
)

