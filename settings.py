CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # If using React
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.utils.autoreload': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
} 