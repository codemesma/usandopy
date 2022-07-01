from django.conf import settings
import os

AWS_ENABLED = getattr(settings, 'AWS_ENABLED', False)
BASE_DIR = getattr(settings, 'BASE_DIR')
# settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
MEDIA_URL = settings.MEDIA_URL if settings.MEDIA_URL else '/media/'
# settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(BASE_DIR + '/media/')
MEDIA_ROOT = settings.MEDIA_ROOT if settings.MEDIA_ROOT else os.path.join(
    BASE_DIR + '/media/')


BLOG_TITLE = "Usando Python"
BLOG_DESCRIPTION = "O site Usando Python é onde você encontra um dos melhores recursos de conteúdo relacionado ao Python para iniciantes que desejam aprender programação, e é um site educacional criado com o objetivo de aumentar o número de desenvolvedores, oferecendo conteúdo gratuito de alta qualidade. Mas o site não se limita apenas ao conteúdo relacionado ao Python, mas também a diversas linguagens, como JavaScript, SQL, HTML, CSS, Dart, Go, linguagem C e muito mais."
BLOG_KEYWORDS = "Usando python, joao Futi Muanda, Joao, usandopy, aulas de python, curso de Python, tutorial de Python,django, python, webframework"
BLOG_AUTHOR = "Joao Futi Muanda"

TUTORIAL_TITLE = "Usando Python"
TUTORIAL_DESCRIPTION = "O site Usando Python é onde você encontra um dos melhores recursos de conteúdo relacionado ao Python para iniciantes que desejam aprender programação, e é um site educacional criado com o objetivo de aumentar o número de desenvolvedores, oferecendo conteúdo gratuito de alta qualidade. Mas o site não se limita apenas ao conteúdo relacionado ao Python, mas também a diversas linguagens, como JavaScript, SQL, HTML, CSS, Dart, Go, linguagem C e muito mais."
TUTORIAL_KEYWORDS = "Usando python, joao Futi Muanda, Joao, usandopy, aulas de python, curso de Python, tutorial de Python"
TUTORIAL_AUTHOR = "Joao Futi Muanda"