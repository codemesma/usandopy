from django.conf import settings
import os

AWS_ENABLED = getattr(settings, 'AWS_ENABLED', False)
BASE_DIR = getattr(settings, 'BASE_DIR')
# settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
MEDIA_URL = settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
# settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(BASE_DIR + '/media/')
MEDIA_ROOT = settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(
    BASE_DIR + '/media/')


BLOG_TITLE = "UsandoPy"
BLOG_DESCRIPTION = "The Usandopy website is where you can find one of the best Python-related content resources for beginners who want to learn programming, and it is an educational website created with the goal of increasing the number of developers by offering free, high-quality content. But the site is not just limited to Python related content but also various languages such as JavaScript, SQL, HTML, CSS, Dart, Go, C language and more."
BLOG_KEYWORDS = "Usando python, joao Futi Muanda, Joao, usandopy, aulas de python, curso de Python, tutorial de Python,django, python, webframework"
BLOG_AUTHOR = "Joao Futi Muanda"

TUTORIAL_TITLE = "UsandoPy"
TUTORIAL_DESCRIPTION = "The Using Python website is where you can find one of the best Python-related content resources for beginners who want to learn programming, and it is an educational website created with the goal of increasing the number of developers by offering free, high-quality content. But the site is not just limited to Python related content but also various languages such as JavaScript, SQL, HTML, CSS, Dart, Go, C language and more."
TUTORIAL_KEYWORDS = "Usando python, joao Futi Muanda, Joao, usandopy, aulas de python, curso de Python, tutorial de Python"
TUTORIAL_AUTHOR = "Joao Futi Muanda"