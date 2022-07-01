from django.conf import settings
import os

AWS_ENABLED = getattr(settings, 'AWS_ENABLED', False)
BASE_DIR = getattr(settings, 'BASE_DIR')
# settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
MEDIA_URL = settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
# settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(BASE_DIR + '/media/')
MEDIA_ROOT = settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(
    BASE_DIR + '/media/')


TUTORIAL_TITLE = "Usando Python"
TUTORIAL_DESCRIPTION = "The Using Python website is where you can find one of the best Python-related content resources for beginners who want to learn programming, and it is an educational website created with the goal of increasing the number of developers by offering free, high-quality content. But the site is not just limited to Python related content but also various languages such as JavaScript, SQL, HTML, CSS, Dart, Go, C language and more."
TUTORIAL_KEYWORDS = "Using python, Girl coder, Girlcoderofficial, usingpy, python lessons, Python course, Python tutorial"
TUTORIAL_AUTHOR = "Usando Python"
