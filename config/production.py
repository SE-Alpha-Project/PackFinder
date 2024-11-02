from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']  # Add your actual domain

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'chaitraleedatar41@gmail.com'
EMAIL_HOST_PASSWORD = 'asqh rowt kron dyui'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER 