# Production settings
from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['iron-yard-grads.herokuapp.com','127.0.0.1']

#Secure Middleware Stuff

SECURE_HSTS_SECONDS = 30
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

#Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
