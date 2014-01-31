from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    HomeView,
    NewsDetailView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^news/(?P<pk>\d+)/$',
        view=NewsDetailView.as_view(),
        name='project.news.detail'
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^captcha/',
        view=include('captcha.urls')
        ),
    url(regex=r'^story/',
        view=include('story.urls')
        ),
    url(regex=r'^article/',
        view=include('templatepages.urls'),
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
