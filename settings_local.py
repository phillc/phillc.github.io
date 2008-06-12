
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Phillip Campbell', 'spyyderz@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'wtflab'             # Or path to database file if using sqlite3.
DATABASE_USER = 'wtflab'             # Not used with sqlite3.
DATABASE_PASSWORD = 'w9t9f9'         # Not used with sqlite3.

CACHE_BACKEND = 'memcached://127.0.0.1:112211/'
CACHE_MIDDLEWARE_SECONDS = 0
CACHE_MIDDLEWARE_KEY_PREFIX = 'wtflab'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

SITE_ID = 1

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
