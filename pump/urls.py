# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .models import (
    PAGE_HOME,
    SECTION_BODY,
)

from .views import (
    DashboardView,
    EventAnonCreateView,
    EventAnonThankyouView,
    EventDetailView,
    EventListView,
    EventPublishView,
    EventRemoveView,
    EventTrustCreateView,
    EventUpdateView,
    StoryAnonCreateView,
    StoryAnonThankyouView,
    StoryDetailView,
    StoryListView,
    StoryPublishView,
    StoryRemoveView,
    StoryTrustCreateView,
    StoryUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^event/$',
        view=EventListView.as_view(),
        name='pump.event.list'
        ),
    url(regex=r'^event/create/anon/$',
        view=EventAnonCreateView.as_view(),
        kwargs=dict(page=PAGE_HOME, section=SECTION_BODY),
        name='pump.event.create.anon'
        ),
    url(regex=r'^event/thankyou/$',
        view=EventAnonThankyouView.as_view(),
        name='pump.event.anon.thankyou'
        ),
    url(regex=r'^event/create/trust/$',
        view=EventTrustCreateView.as_view(),
        kwargs=dict(page=PAGE_HOME, section=SECTION_BODY),
        name='pump.event.create.trust'
        ),
    url(regex=r'^event/(?P<pk>\d+)/$',
        view=EventDetailView.as_view(),
        name='pump.event.detail'
        ),
    url(regex=r'^event/(?P<pk>\d+)/publish/$',
        view=EventPublishView.as_view(),
        name='pump.event.publish'
        ),
    url(regex=r'^event/(?P<pk>\d+)/remove/$',
        view=EventRemoveView.as_view(),
        name='pump.event.remove'
        ),
    url(regex=r'^event/(?P<pk>\d+)/edit/$',
        view=EventUpdateView.as_view(),
        name='pump.event.update'
        ),
    url(regex=r'^story/create/anon/$',
        view=StoryAnonCreateView.as_view(),
        kwargs=dict(page=PAGE_HOME, section=SECTION_BODY),
        name='pump.story.create.anon'
        ),
    url(regex=r'^story/thankyou/$',
        view=StoryAnonThankyouView.as_view(),
        name='pump.story.anon.thankyou'
        ),
    url(regex=r'^story/create/trust/$',
        view=StoryTrustCreateView.as_view(),
        kwargs=dict(page=PAGE_HOME, section=SECTION_BODY),
        name='pump.story.create.trust'
        ),
    url(regex=r'^story/(?P<pk>\d+)/$',
        view=StoryDetailView.as_view(),
        name='pump.story.detail'
        ),
    url(regex=r'^$',
        view=DashboardView.as_view(),
        name='pump.dashboard'
        ),
    url(regex=r'^story/$',
        view=StoryListView.as_view(),
        name='pump.story.list'
        ),
    url(regex=r'^story/(?P<pk>\d+)/publish/$',
        view=StoryPublishView.as_view(),
        name='pump.story.publish'
        ),
    url(regex=r'^story/(?P<pk>\d+)/remove/$',
        view=StoryRemoveView.as_view(),
        name='pump.story.remove'
        ),
    url(regex=r'^story/(?P<pk>\d+)/edit/$',
        view=StoryUpdateView.as_view(),
        name='pump.story.update'
        ),
)
