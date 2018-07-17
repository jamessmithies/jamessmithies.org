try:
	from project.settings.base import *
	from project.settings.secrets import *
except ImportError:
    pass

import os
PROJECT_PATH = os.getcwd()

DEBUG = True

STATIC_ROOT = 'collectstatic'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
MEDIA_URL = '/media/'




