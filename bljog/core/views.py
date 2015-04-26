from django.shortcuts import render

from blog.models import Post


def index(request):
    recent_posts = Post.objects.all().order_by('-created')[:5]
    return render(request, 'core/home.html', context={'recent_posts': recent_posts})
