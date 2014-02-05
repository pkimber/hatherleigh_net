from django.conf.urls import (
    patterns, url
)

from .views import (
    EventAnonCreateView,
    StoryAnonCreateView,
    StoryDetailView,
    StoryListView,
    StoryPublishView,
    StoryRemoveView,
    StoryTrustCreateView,
    StoryUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^event/create/anon/$',
        view=EventAnonCreateView.as_view(),
        kwargs=dict(page='home', layout='body'),
        name='pump.event.create.anon'
        ),
    url(regex=r'^story/create/anon/$',
        view=StoryAnonCreateView.as_view(),
        kwargs=dict(page='home', layout='body'),
        name='pump.story.create.anon'
        ),
    url(regex=r'^create/trust/$',
        view=StoryTrustCreateView.as_view(),
        kwargs=dict(page='home', layout='body'),
        name='pump.story.create.trust'
        ),
    url(regex=r'^(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='pump.story.detail'
        ),
    url(regex=r'^$',
        view=StoryListView.as_view(),
        name='pump.story.list'
        ),
    url(regex=r'^(?P<pk>\d+)/publish/$',
        view=StoryPublishView.as_view(),
        name='pump.story.publish'
        ),
    url(regex=r'^(?P<pk>\d+)/remove/$',
        view=StoryRemoveView.as_view(),
        name='pump.story.remove'
        ),
    url(regex=r'^(?P<pk>\d+)/edit/$',
        view=StoryUpdateView.as_view(),
        name='pump.story.update'
        ),
)
