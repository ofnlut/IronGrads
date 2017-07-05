# Production settings
from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']



#Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
