from django.db import models


# TODO: Mutable field for user-specified order.
class Link(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=60)