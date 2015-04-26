from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from autoslug import AutoSlugField

from comments.models import Comment

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from='title', unique=True)
    body = models.TextField(blank=True)
    comments = GenericRelation(Comment)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title