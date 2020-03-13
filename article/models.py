from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField
from PIL import Image


class ArticleCategory(models.Model):
    articleCategory = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.articleCategory


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArticleCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MDTextField()
    tags = TaggableManager(blank=True)
    like = models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        article = super(Article, self).save(*args, **kwargs)

        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            image.save(self.avatar.path)

        return article

    class Meta:
        verbose_name = "article"
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title
