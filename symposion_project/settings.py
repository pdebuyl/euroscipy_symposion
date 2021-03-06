# -*- coding: utf-8 -*-
# Django settings for account project

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = False

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = True

INTERNAL_IPS = [
    "127.0.0.1",
]

DEFAULT_HTTP_PROTOCOL = "https"

ADMINS = [
    ("Pierre de Buyl", "pdebuyl@ulb.ac.be"),
]

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Berlin"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "symposion_project.urls"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinax_utils.context_processors.settings",
    "account.context_processors.account",
    "symposion.reviews.context_processors.reviews",
    'plata.context_processors.plata_context',
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    
    # theme
    "pinax_theme_bootstrap_account",
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    
    # external
    "debug_toolbar",
    "mailer",
    "timezones",
    "metron",
    "markitup",
    "taggit",
    "reversion",
    "easy_thumbnails",
    "sitetree",
    "account",
    
    # symposion
    "symposion",
    "symposion.sponsorship",
    "symposion.conference",
    "symposion.cms",
    "symposion.boxes",
    "symposion.proposals",
    "symposion.speakers",
    "symposion.teams",
    "symposion.reviews",
    "symposion.schedule",
    
    # project
    "symposion_project.proposals",

    # plata
    'plata',
    'plata.contact',
    'plata.discount',
    'plata.payment',
    'plata.product',
    'plata.shop',

    'plata_simple',

]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

#EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.email

AUTHENTICATION_BACKENDS = [
    # Permissions Backends
    "symposion.teams.backends.TeamPermissionsBackend",
    
    # Auth backends
    "account.auth_backends.EmailAuthenticationBackend",
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

MARKITUP_FILTER = ("markdown.markdown", {"safe_mode": True, "extensions":['extra']})
MARKITUP_SET = "markitup/sets/markdown"
MARKITUP_SKIN = "markitup/skins/simple"

CONFERENCE_ID = 1

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"

PROPOSAL_FORMS = {
    "tutorial": "symposion_project.proposals.forms.TutorialProposalForm",
    "talk": "symposion_project.proposals.forms.TalkProposalForm",
    "poster": "symposion_project.proposals.forms.PosterProposalForm",
}

SYMPOSION_VOTE_THRESHOLD = 2

# PLATA settings

#PLATA_PRICE_INCLUDES_TAX = False

PLATA_PAYMENT_MODULES = [ 'plata.payment.modules.ogone.PaymentProcessor' ]

# PLATA settings

TEST_RUNNER = 'options.test_utils.test_runner_with_coverage'
COVERAGE_MODULES = ['plata']

import logging, sys
logging.basicConfig(
    filename=os.path.join(PROJECT_ROOT,'plata.log'),
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
    level=logging.DEBUG,
    )

PLATA_SHOP_PRODUCT = 'plata_simple.Product'
CURRENCIES = ('EUR',)

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
