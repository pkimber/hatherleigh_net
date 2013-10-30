from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

TEMPLATE_STRING_IF_INVALID = '**** INVALID EXPRESSION: %s ****'

# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
MEDIA_ROOT = 'media'

# The production site has custom templates and static media uploaded using
# FTP.  We have some example templates for testing purposes.
TEMPLATE_DIRS = (
    os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '..',
            'example',
            'templates',
        )
    ),
)

# Django debug toolbar (this is the address of the client not the server)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
