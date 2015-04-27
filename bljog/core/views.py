from django.shortcuts import render
from django.views.generic.base import ContextMixin, TemplateView

from blog.models import Post
from .models import Link


# def index(request):
#     recent_posts = Post.objects.all().order_by('-created')[:3]
#     return render(request, 'core/home.html', context={'recent_posts': recent_posts})


class ArchivedPostsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archived_posts'] = Post.objects.list_archived_months()

        return context


class LinksMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = Link.objects.all()

        return context


class RecentPostsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.order_by('-created')[:5]

        return context


class HomeView(RecentPostsMixin, LinksMixin, ArchivedPostsMixin, TemplateView):
    template_name = 'core/home.html'