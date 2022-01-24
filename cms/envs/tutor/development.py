# -*- coding: utf-8 -*-
import os
from cms.envs.devstack import *

LMS_BASE = "testnewrelease.xyz:8000"
LMS_ROOT_URL = "http://" + LMS_BASE

# Authentication
SOCIAL_AUTH_EDX_OAUTH2_KEY = "cms-sso-dev"
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = LMS_ROOT_URL

FEATURES["PREVIEW_LMS_BASE"] = "preview.testnewrelease.xyz:8000"

####### Settings common to LMS and CMS
import json
import os

from xmodule.modulestore.modulestore_settings import update_module_store_settings

# Mongodb connection parameters: simply modify `mongodb_parameters` to affect all connections to MongoDb.
mongodb_parameters = {
    "host": "mongodb",
    "port": 27017,
    
    "user": None,
    "password": None,
    
    "db": "openedx",
}
DOC_STORE_CONFIG = mongodb_parameters
CONTENTSTORE = {
    "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
    "ADDITIONAL_OPTIONS": {},
    "DOC_STORE_CONFIG": DOC_STORE_CONFIG
}
# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)
DATA_DIR = "/openedx/data/modulestore"

for store in MODULESTORE["default"]["OPTIONS"]["stores"]:
   store["OPTIONS"]["fs_root"] = DATA_DIR

# Behave like memcache when it comes to connection errors
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# Elasticsearch connection parameters
ELASTIC_SEARCH_CONFIG = [{
  
  "host": "elasticsearch",
  "port": 9200,
}]

CONTACT_MAILING_ADDRESS = "tehsilim.edu.az - http://testnewrelease.xyz"

DEFAULT_FROM_EMAIL = ENV_TOKENS.get("DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS.get("DEFAULT_FEEDBACK_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
SERVER_EMAIL = ENV_TOKENS.get("SERVER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
TECH_SUPPORT_EMAIL = ENV_TOKENS.get("TECH_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
CONTACT_EMAIL = ENV_TOKENS.get("CONTACT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BUGS_EMAIL = ENV_TOKENS.get("BUGS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
UNIVERSITY_EMAIL = ENV_TOKENS.get("UNIVERSITY_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PRESS_EMAIL = ENV_TOKENS.get("PRESS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS.get("PAYMENT_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BULK_EMAIL_DEFAULT_FROM_EMAIL = ENV_TOKENS.get("BULK_EMAIL_DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS.get("API_ACCESS_MANAGER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_FROM_EMAIL = ENV_TOKENS.get("API_ACCESS_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])

# Get rid completely of coursewarehistoryextended, as we do not use the CSMH database
INSTALLED_APPS.remove("lms.djangoapps.coursewarehistoryextended")
DATABASE_ROUTERS.remove(
    "openedx.core.lib.django_courseware_routers.StudentModuleHistoryExtendedRouter"
)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Add your MFE and third-party app domains here
CORS_ORIGIN_WHITELIST = []

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]
# Silence some loggers (note: we must attempt to get rid of these when upgrading from one release to the next)

import warnings
from django.utils.deprecation import RemovedInDjango40Warning, RemovedInDjango41Warning
warnings.filterwarnings("ignore", category=RemovedInDjango40Warning)
warnings.filterwarnings("ignore", category=RemovedInDjango41Warning)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="lms.djangoapps.course_wiki.plugins.markdownedx.wiki_plugin")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="wiki.plugins.links.wiki_plugin")

# Email
EMAIL_USE_SSL = False
# Forward all emails from edX's Automated Communication Engine (ACE) to django.
ACE_ENABLED_CHANNELS = ["django_email"]
ACE_CHANNEL_DEFAULT_EMAIL = "django_email"
ACE_CHANNEL_TRANSACTIONAL_EMAIL = "django_email"
EMAIL_FILE_PATH = "/tmp/openedx/emails"

# Language/locales
LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")
LANGUAGE_COOKIE_NAME = "openedx-language-preference"

# Allow the platform to include itself in an iframe
X_FRAME_OPTIONS = "SAMEORIGIN"


JWT_AUTH["JWT_ISSUER"] = "http://testnewrelease.xyz/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "huHlYF0YbCaIoa2ByKduRKeA"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "AscVTrng7k9IdfDhMFZBmLpcWY-Ydwf5AK3hAMSUK3cfXHN8_iW_mw7Hcq1f6g1ge6C6WfdTakKvKKD1gSYLPzSwtImsC6AB4Ccra71jg1oEG8HbvOOT5jFlua5xweEtPB7F5_btaNjwzGia5WB8_uqYA7A9zLSjGtgI9Dfl5st_NEr3pqz4DRSOyg800hX4bVKKfoqdCna-4mNvkWeoucQq5nEjg6EuI9KVWp74KImUX_1WMcydA9hr8l6IRds0SlVrFNaotVpweuIBR8GPZql_2ONbG8PryNDWgZJmf8vmjyh7jkmLuvsoypZUbX1jFgIizpL_Ro3VWOsFTvAH3w",
        "n": "rKG0c9iWkAOV9tt-qBqwPxwPCFy-e6z7LnYmwd734MD1lCyI1VTJsa3S9KsNk8uxGef1-OGgAXsQdn_4vjipRUuZ2X3GSwdIgWgqdmzSavJlLf8mLL8CAgOfJ329UTCz9sbVkranNpYwJy8MvbIpXnV7wmYU3YLti4E5uBq71Cl06BZ1zj_o9e3sbmw_InZA2P4HcsWiohJoDiNMYOEZMoQ_Mrzmi9R5L9SC88Ofq2RAx8-8suEufgjALoHo5woXe__gaoODf23hEjMEU95NJUyWhs7vBahqvaE2H-czurgsPu6qAJrJ3Oo4w-_j5_WePwVJ-U6RVk6SdNr64rTfhQ",
        "p": "zdCqSDNRXNNnpaP4x9hfTv8UJarS-6ncfm1q0Q1gCSkGMyggDlDzAlnxrTE9wpFdBqSf7yauCayFtk0x-oY9arTRQjHaCQu3b4bRXBn13zmQkmlOAJgxgg63VY0kYavfw_D-w-0am5E1gIcZMVpz5J3O6Wft8sSB-DKYot6IUxM",
        "q": "1rmsCj9g9T3uVbFTVARYIAcTj7SAC5Qew9g8rhqFCWEJWyhXqoY2nFe2m7A8mdpdbm_4xWHDB5MitbCkYVs4q-tN1aG5ARCBcF-vygdzYGSoWXnT9Y9S2HtLopFTvIZu9ZTv2MecVneshVFSv7TCSIZVIeHnJmLrGBLUb5M0Pgc",
    }
)
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "rKG0c9iWkAOV9tt-qBqwPxwPCFy-e6z7LnYmwd734MD1lCyI1VTJsa3S9KsNk8uxGef1-OGgAXsQdn_4vjipRUuZ2X3GSwdIgWgqdmzSavJlLf8mLL8CAgOfJ329UTCz9sbVkranNpYwJy8MvbIpXnV7wmYU3YLti4E5uBq71Cl06BZ1zj_o9e3sbmw_InZA2P4HcsWiohJoDiNMYOEZMoQ_Mrzmi9R5L9SC88Ofq2RAx8-8suEufgjALoHo5woXe__gaoODf23hEjMEU95NJUyWhs7vBahqvaE2H-czurgsPu6qAJrJ3Oo4w-_j5_WePwVJ-U6RVk6SdNr64rTfhQ",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://testnewrelease.xyz/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "huHlYF0YbCaIoa2ByKduRKeA"
    }
]

# Enable/Disable some features globally
FEATURES["ENABLE_DISCUSSION_SERVICE"] = False
FEATURES["PREVENT_CONCURRENT_LOGINS"] = False

# Disable codejail support
# explicitely configuring python is necessary to prevent unsafe calls
import codejail.jail_code
codejail.jail_code.configure("python", "nonexistingpythonbinary", user=None)
# another configuration entry is required to override prod/dev settings
CODE_JAIL = {
    "python_bin": "nonexistingpythonbinary",
    "user": None,
}


######## End of settings common to LMS and CMS

######## Common CMS settings

STUDIO_NAME = u"tehsilim.edu.az - Studio"

# Authentication
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "nRF5oReBo9qsY7bvhiJfNFpj"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = "http://lms:8000"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False  # scheme is correctly included in redirect_uri

MAX_ASSET_UPLOAD_FILE_SIZE_IN_MB = 100

FRONTEND_LOGIN_URL = LMS_ROOT_URL + '/login'
FRONTEND_LOGOUT_URL = LMS_ROOT_URL + '/logout'
FRONTEND_REGISTER_URL = LMS_ROOT_URL + '/register'

# Create folders if necessary
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common CMS settings

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"


