# Production settings (This should never change)
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

#Secure Middleware Settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 10 #Careful with this
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

#Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
