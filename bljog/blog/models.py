from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)
    comments = generic.GenericRelation('Comment')
