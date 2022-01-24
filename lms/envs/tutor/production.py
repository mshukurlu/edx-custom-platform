# -*- coding: utf-8 -*-
import os
from lms.envs.production import *

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

CONTACT_MAILING_ADDRESS = "tehsilim.edu.az - http://local.overhang.io"

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


JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "r57ssnG4eCYGvbN2SECVl6CD"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "BSgZzi4H75ov6BACIld7qbDtae527TA9Kbg7U0bFZC37d4MnL6ZHafj2uvkq7m4Nj9z_UE8WMillvyB-u1kqrxt6yVF7qapmlWl9GcB9MmgL6XfUqLdQNlOMh2lXfHpkFZBf1iA90KjZV5iVXDV58dZgimNLzdvL36F1txikrg20S4vfgBFXDhVZfSZHtC9uDeqHjmb2tNlHEGd5VedjWTUhyrW1m4Ye05l4WXUZid0X-gACl3HITfDrPigVUl9Y7xxbSrMWp6jQMLsnoQvyFJIiEOZnMITYRbUEcQMhGItHWpKdcQ5ubiP5jslOmi58CAUhZbt4j9Y1wyKTwM5RoQ",
        "n": "t-isge11sg7dpw0fa_9GthRhzio_XdX6CBtzZLVPbc1aQnRlJBdGIww-9dgIMPO9SSIZtDbZDhjzs78PlMVwC47O2bLm6qqNg9rnJwGGejXuJ_l_dpQicYizZpJKlyoYSi2OHMPPFnAspFJ-mxZd98wsPZvjoTZLXyQTBh-7Y2rl2zNAuLLmIvvpKIETAHZRrRVB0PYhpN1fOuIKvBuFK-F_YyaSbxClRuJD8OOkWMfUZmcbrresHDtQNe6NyOvuGwRAQx6_EDX0vlBSuQjf0NRDMq5ewHvbvsm6dhJlNwcJEEgQw2kNk24ggc6lkkt8gArcibt_pBiXzsYIb143Nw",
        "p": "0IjugcaLYs2abd5J216T0WJixGye3nCFcj4sS2frcJBv8SROFBaplbAjpZ87o9n90lkzmEno51YF41NbP62KzZtfMritSzOTL0CjQeBrwN6tDSASWvgB7AK5w8fl612SjWtC06SwdVvTadaEepdHO92rHq7h0IbYaxVfLh27ePs",
        "q": "4cTQv4LsAndtk-gPiKWu7Bla6HoOjebjXIlzo2LMYaW90LEKJ-lTOtCLsWoyOl7h0yVjPiXl36wSCtOfoyKkUPicXAV8hTMVXNju4eXS9hVXb5qfyqXsD-wj8rhDljQC7hGFZ2e9Az2fNqysfvkxhvHJiGfvp4VK_Edz75SNHfU",
    }
)
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "t-isge11sg7dpw0fa_9GthRhzio_XdX6CBtzZLVPbc1aQnRlJBdGIww-9dgIMPO9SSIZtDbZDhjzs78PlMVwC47O2bLm6qqNg9rnJwGGejXuJ_l_dpQicYizZpJKlyoYSi2OHMPPFnAspFJ-mxZd98wsPZvjoTZLXyQTBh-7Y2rl2zNAuLLmIvvpKIETAHZRrRVB0PYhpN1fOuIKvBuFK-F_YyaSbxClRuJD8OOkWMfUZmcbrresHDtQNe6NyOvuGwRAQx6_EDX0vlBSuQjf0NRDMq5ewHvbvsm6dhJlNwcJEEgQw2kNk24ggc6lkkt8gArcibt_pBiXzsYIb143Nw",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "r57ssnG4eCYGvbN2SECVl6CD"
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

######## Common LMS settings
LOGIN_REDIRECT_WHITELIST = ["studio.local.overhang.io"]

# Better layout of honor code/tos links during registration
REGISTRATION_EXTRA_FIELDS["terms_of_service"] = "required"
REGISTRATION_EXTRA_FIELDS["honor_code"] = "hidden"

# Fix media files paths
PROFILE_IMAGE_BACKEND["options"]["location"] = os.path.join(
    MEDIA_ROOT, "profile-images/"
)

COURSE_CATALOG_VISIBILITY_PERMISSION = "see_in_catalog"
COURSE_ABOUT_VISIBILITY_PERMISSION = "see_about_page"

# Allow insecure oauth2 for local interaction with local containers
OAUTH_ENFORCE_SECURE = False

# Email settings
class LazyStaticAbsoluteUrl:
    """
    Evaluates a static asset path lazily at runtime
    """
    def __init__(self, path):
        self.path = path

    def __str__(self):
        from django.conf import settings
        from django.contrib.staticfiles.storage import staticfiles_storage
        return settings.LMS_ROOT_URL + staticfiles_storage.url(self.path)

    def to_json(self):
        # This method is required for json serialization by edx-ace, notably for
        # serialization of the registration email. See
        # edx_ace.serialization.MessageEncoder.
        return str(self)
# We need a lazily-computed logo url to capture the url of the theme-specific logo.
DEFAULT_EMAIL_LOGO_URL = LazyStaticAbsoluteUrl("images/logo.png")

# Create folders if necessary
for folder in [DATA_DIR, LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE, ORA2_FILEUPLOAD_ROOT]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common LMS settings

ALLOWED_HOSTS = [
    ENV_TOKENS.get("LMS_BASE"),
    FEATURES["PREVIEW_LMS_BASE"],
    "lms",
]


# When we cannot provide secure session/csrf cookies, we must disable samesite=none
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = "Lax"


# CMS authentication
IDA_LOGOUT_URI_LIST.append("http://studio.local.overhang.io/complete/logout")

# Required to display all courses on start page
SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True


ACCOUNT_MICROFRONTEND_URL = "http://apps.local.overhang.io/account"


WRITABLE_GRADEBOOK_URL = "http://apps.local.overhang.io/gradebook"


LEARNING_MICROFRONTEND_URL = "http://apps.local.overhang.io/learning"


PROFILE_MICROFRONTEND_URL = "http://apps.local.overhang.io/profile/u/"


LOGIN_REDIRECT_WHITELIST.append("apps.local.overhang.io")
CORS_ORIGIN_WHITELIST.append("http://apps.local.overhang.io")
CSRF_TRUSTED_ORIGINS.append("apps.local.overhang.io")