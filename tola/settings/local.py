"""Development settings and globals."""
from os.path import join, normpath
from base import *
#import os, yaml
#
#from base import *
#
#def read_yaml(path):
#    with open(path) as f:
#        data = yaml.load(f)
#    return data
#
#SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
#CONFIG_DIR = os.path.abspath(os.path.join(SETTINGS_DIR,
#                                          os.pardir,
#                                          os.pardir,
#                                          'config'))
#app_settings = read_yaml(os.path.join(CONFIG_DIR, './settings.secret.yml'))

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('django', 'admin', 'tola@tola.org'),
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# ALLOWED HOSTS
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = (
   "localhost",
   "www.mercycorps.org",
   "www.google.com",
   "*.github.com",
   "www.github.com",
   "api.github.com",
   "tola-activity-dev.mercycorps.org",
   "tola-activity-demo.mercycorps.org",
   "tola-activity.mercycorps.org",
   "tola-tables.mercycorps.org",
   "tola-tables-dev.mercycorps.org",
   "tola-tables-demo.mercycorps.org",
   "tables.toladata.io",
   "mc-tables.toladata.io",
   "178.62.204.85" )

# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tolatables',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dbp',
        'PASSWORD': 'ttmTolaTabl3s2016',
        'HOST': 'mysqldb',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

MONGODB_HOST = 'mongodb://mongodb/tola'
MONGODB_NAME = 'tola'



# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
#DEBUG = app_settings['DEBUG']
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = False

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

EMAIL_FILE_PATH = "/tmp/tola-messages"

# GOOGLE CLIENT CONFIG
GOOGLE_REDIRECT_URL = "https://tables.toladata.io"
GOOGLE_STEP2_URI = "https://tables.toladata.io/gwelcome"
GOOGLE_CLIENT_ID = "445847194486-s6v6mntl2fhn7ve5d0ubolsnvm57l03k.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "vjFMy47999sHMoNd_DZSdmPK"


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "445847194486-s6v6mntl2fhn7ve5d0ubolsnvm57l03k.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "vjFMy47999sHMoNd_DZSdmPK"
#SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS:


TOLA_TABLES_USER = "445847194486-s6v6mntl2fhn7ve5d0ubolsnvm57l03k.apps.googleusercontent.com"
TOLA_TABLES_TOKEN = "vjFMy47999sHMoNd_DZSdmPK"

# LOCAL APPS DEPENDING ON SERVER DEBUG FOR DEV BOXES,
# REPORT BUILDER FOR REPORT SERVER
#DEV_APPS = app_settings['DEV_APPS']

#INSTALLED_APPS = INSTALLED_APPS + tuple(DEV_APPS)


LDAP_LOGIN = 'uid=pluma,ou=People,dc=system,dc=mercycorps,dc=org'
LDAP_SERVER = 'ldaps://ldap.mercycorps.org' # ldap prod
LDAP_PASSWORD = 'mc2Plum4pw!' # ldap prod
LDAP_USER_GROUP = 'ertb'
LDAP_ADMIN_GROUP = 'ertb-admin'
#####################


SECRET_KEY = 'r"!0^+)=t*ly6ycprf9@kfw$6fsjd0xoh#pa*2erx1m*lp5k9ko7"'

##### WHEN MC SERVER ADD COSIGN #####
AUTHENTICATION_BACKENDS = (
  'social.backends.google.GoogleOAuth2',
  'django.contrib.auth.backends.ModelBackend' )

#### NON_LDAP: False then activate cosign for MC ####
#### OFFLINE_MODE only for raspberry pi ####
# If report server then limit navigation and allow access to public dashboards
REPORT_SERVER = False
OFFLINE_MODE = False
NON_LDAP = True




#############################################################################################################################################################################################################
###################################################################################################################################################################################################
###################################################################################################################################################################################################
#########################################################################################################################################################################################################


