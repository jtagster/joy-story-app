from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

VISIBILITY = (
    ('PRIVATE', 'only me'),
    ('PUBLIC', 'everyone'),
    )

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
    public = models.CharField(max_length=7, choices=VISIBILITY, default='PRIVATE')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def share(self):
        self.public = 'PUBLIC'
        self.save()
    
    def unshare(self):
        self.public = 'PRIVATE'
        self.save()
    
    def __str__(self):
        return self.title


#our helper
def get_image_path(instance, filename):
    return '/'.join(['post_images', instance.post.slug, filename])
    
class Upload(models.Model):
    post = models.ForeignKey(Post, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)
        