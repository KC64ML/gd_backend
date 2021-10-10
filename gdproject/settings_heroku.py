# coding: utf-8
from gdproject.settings import *

# for production server, do not use debug mode on production environment
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_d219501a8ebf168',
        'USER': 'bfc96653faaba1',
        'PASSWORD': 'dfc6fc80',
        'HOST': 'us-cdbr-east-04.cleardb.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
        'CONN_MAX_AGE': 5,
    }
}
