from django.conf.urls import include, url
from django.contrib import admin

from core.views import HomeView

# TODO: Name views and factor out into per-app includes.
urlpatterns = [
    # Examples:
    # url(r'^$', 'bljog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
]
