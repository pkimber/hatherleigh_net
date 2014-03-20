# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView,
    TemplateView,
)

from base.view_utils import BaseMixin

from pump.models import StoryBlock


class HomeView(BaseMixin, TemplateView):

    template_name = 'home.html'


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
