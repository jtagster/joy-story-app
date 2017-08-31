from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    gratitudeStmt = models.CharField(max_length=255)
    emotionTags = models.CharField(max_length = 500)
    sensationTags = models.CharField(max_length = 500)
    story = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slug = models.SlugField(unique=True)
    public = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title