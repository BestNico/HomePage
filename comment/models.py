from django.db import models
from django.contrib.auth.models import User
from article.models import Article


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.CharField(max_length=20, blank=False)
    mail = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.message[:20]
