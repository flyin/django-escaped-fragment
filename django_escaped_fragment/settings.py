from django.conf import settings


USER_SETTINGS = getattr(settings, 'CRAWLER_SETTINGS', None)

DEFAULTS = {
    'SITE_URL': 'http://localhost',
    'USE_CACHE': True,
    'CACHE_TIMEOUT': 300,
    'PHANTOMJS_PORT': 64738,
    'DELETE_FRAGMENT_FROM_RENDERED': True,
}

crawler_settings = DEFAULTS.copy()
crawler_settings.update(USER_SETTINGS)
