# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    HomeView,
    StoryDetailView,
    StoryMonthArchiveView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^story/(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='project.story.detail'
        ),
    url(regex=r'^story/(?P<year>\d{4})/(?P<month>[-\w]+)/$',
        view=StoryMonthArchiveView.as_view(),
        name='project.story.archive'
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
    url(regex=r'^pump/',
        view=include('pump.urls')
        ),
    url(regex=r'^article/',
        view=include('templatepages.urls'),
        kwargs=dict(
            extra_context=dict(today=datetime.today(),)
        )),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
