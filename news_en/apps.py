from django.apps import AppConfig


class News_enConfig(AppConfig):
    name = 'news_en'

    def ready(self):
        from news.signals import save_news_slug, save_category_slug

