from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField

class ArticleCategory(models.Model):
    articleCategory = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.articleCategory


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArticleCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = MDTextField()
    tags = TaggableManager(blank=True)
    like = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "article"
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title
