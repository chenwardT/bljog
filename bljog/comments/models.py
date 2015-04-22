from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()