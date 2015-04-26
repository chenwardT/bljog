from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    fields = (('author', 'title', 'published'), 'body')
    list_display = ('author', 'title', 'created', 'modified', 'published')