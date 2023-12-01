from django.db import models

class CachedNews(models.Model):
    date_cached = models.DateField(auto_now_add=True)
    news_data = models.JSONField()