from django.db import models
from django.shortcuts import reverse
from news_en.models import News, Category


class SiteSettings(models.Model):
    sitename = models.CharField(max_length=250,blank=False)

    def __str__(self):
        return self.sitename

class HomePageSettings(models.Model):
    hot_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='hot_news_en',blank=True,null=True)
    trending = models.ForeignKey(News, on_delete=models.CASCADE, related_name='trending_en',blank=True,null=True)
    editor_choice = models.ForeignKey(News, on_delete=models.CASCADE, related_name='editor_choice_en',blank=True,null=True)
    post_catalog_one = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_one_en',blank=True,null=True)
    post_catalog_two = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_two_en',blank=True,null=True)
    post_catalog_three = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_three_en',blank=True,null=True)
    post_catalog_four = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_four_en',blank=True,null=True)
    post_catalog_five = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_five_en',blank=True,null=True)



class SocialSetting(models.Model):
    icon = models.CharField(max_length=20)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.name
