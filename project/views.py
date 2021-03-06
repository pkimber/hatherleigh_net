# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView,
    TemplateView,
)
from django.views.generic.dates import MonthArchiveView

from base.view_utils import BaseMixin

from pump.models import (
    get_home_body,
    Story,
    StoryBlock,
)


class HomeView(BaseMixin, TemplateView):

    template_name = 'home.html'


class StoryMonthArchiveView(BaseMixin, MonthArchiveView):

    allow_empty = True
    date_field = 'story_date'
    make_object_list = True
    allow_future = True
    template_name = 'story_archive_month.html'

    def get_queryset(self):
        home_body = get_home_body()
        return Story.objects.published(home_body)


class StoryDetailView(BaseMixin, DetailView):

    model = StoryBlock
    template_name = 'story.html'

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        story = get_object_or_404(
            self.object.content,
            moderate_state__slug='published'
        )
        context.update(dict(
            story=story,
        ))
        return context
