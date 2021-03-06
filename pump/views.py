# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
)

from braces.views import LoginRequiredMixin

from base.view_utils import BaseMixin
from block.forms import ContentEmptyForm
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    EventAnonForm,
    EventTrustForm,
    StoryAnonForm,
    StoryTrustForm,
)
from .models import (
    Event,
    EventBlock,
    get_home_body,
    Story,
    StoryBlock,
)


def check_perm(user, story):
    """user must be a member of staff or have created the story"""
    if user.is_staff:
        pass
    elif not story.user == user:
        # the user did not create the story
        raise PermissionDenied()


class CheckPermMixin(object):

    def _check_perm(self, story):
        check_perm(self.request.user, story)


class EventAnonCreateView(ContentCreateView):

    block_class = EventBlock
    form_class = EventAnonForm
    model = Event
    template_name = 'pump/event_form_text_only.html'

    def get(self, request, *args, **kwargs):
        """
        If a user is logged in (and active), they shouldn't be using this
        view... they can use the view for a logged in user.
        """
        if self.request.user and self.request.user.is_active:
            return HttpResponseRedirect(reverse('pump.event.create.trust'))
        else:
            return super(EventAnonCreateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('pump.event.anon.thankyou')


class EventAnonThankyouView(BaseMixin, TemplateView):

    template_name = 'event_thankyou.html'


class EventDetailView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, DetailView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        self._check_perm(self.object)
        context.update(dict(
            user_can_edit=self.object.user_can_edit(self.request.user),
        ))
        return context


class EventListView(LoginRequiredMixin, BaseMixin, ListView):
    """List of events for a logged in user.

    We have a 'context_object_name' because the 'pending' method returns a
    list of event instances, not a queryset.

    """

    context_object_name = 'event_list'
    template_name = 'pump/event_list.html'

    def get_queryset(self):
        home_body = get_home_body()
        if self.request.user.is_staff:
            result = Event.objects.pending(home_body)
        else:
            result = Event.objects.pending(
                home_body,
                dict(user=self.request.user)
            )
        return result


class EventPublishView(LoginRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Event
    template_name = 'pump/event_publish_form.html'

    def get_success_url(self):
        return reverse('pump.event.list')


class EventRemoveView(LoginRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Event
    template_name = 'pump/event_remove_form.html'

    def get_success_url(self):
        return reverse('pump.event.list')


class EventTrustCreateView(LoginRequiredMixin, ContentCreateView):

    block_class = EventBlock
    form_class = EventTrustForm
    model = Event
    template_name = 'pump/event_form_wysiwyg.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(EventTrustCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('pump.event.list')


class EventUpdateView(
        LoginRequiredMixin, CheckPermMixin, ContentUpdateView):

    model = Event
    form_class = EventTrustForm
    template_name = 'pump/event_form_wysiwyg.html'

    def get_object(self, *args, **kwargs):
        obj = super(EventUpdateView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        if not obj.user_can_edit(self.request.user):
            raise PermissionDenied()
        return obj

    def get_success_url(self):
        return self.object.get_absolute_url()


class DashboardView(LoginRequiredMixin, BaseMixin, TemplateView):
    """List of events and stories for the logged in user."""

    template_name = 'pump/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        home_body = get_home_body()
        if self.request.user.is_staff:
            event_list = Event.objects.pending(home_body)
            story_list = Story.objects.pending(home_body)
        else:
            event_list = Event.objects.pending(
                home_body,
                dict(user=self.request.user)
            )
            story_list = Story.objects.pending(
                home_body,
                dict(user=self.request.user)
            )
        context.update(dict(
            event_list=event_list,
            story_list=story_list,
        ))
        return context


class StoryAnonCreateView(ContentCreateView):

    block_class = StoryBlock
    form_class = StoryAnonForm
    model = Story
    template_name = 'pump/story_form_text_only.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.story_date = datetime.now()
        return super(StoryAnonCreateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        """
        If a user is logged in (and active), they shouldn't be using this
        view... they can use the view for a logged in user.
        """
        if self.request.user and self.request.user.is_active:
            return HttpResponseRedirect(reverse('pump.story.create.trust'))
        else:
            return super(StoryAnonCreateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('pump.story.anon.thankyou')


class StoryAnonThankyouView(BaseMixin, TemplateView):

    template_name = 'story_thankyou.html'


class StoryTrustCreateView(LoginRequiredMixin, ContentCreateView):

    block_class = StoryBlock
    form_class = StoryTrustForm
    model = Story
    template_name = 'pump/story_form_wysiwyg.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.story_date = datetime.now()
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('pump.story.list')


class StoryDetailView(
        LoginRequiredMixin, CheckPermMixin, BaseMixin, DetailView):

    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        self._check_perm(self.object)
        context.update(dict(
            user_can_edit=self.object.user_can_edit(self.request.user),
        ))
        return context


class StoryListView(LoginRequiredMixin, BaseMixin, ListView):
    """List of stories for a logged in user.

    We have a 'context_object_name' because the 'pending' method returns a
    list of contact instances, not a queryset.

    """

    context_object_name = 'story_list'
    template_name = 'pump/story_list.html'

    def get_queryset(self):
        home_body = get_home_body()
        if self.request.user.is_staff:
            result = Story.objects.pending(
                home_body,
                dict(
                    order_by='-order',
                )
            )
        else:
            result = Story.objects.pending(
                home_body,
                dict(
                    order_by='-order',
                    user=self.request.user,
                )
            )
        return result


class StoryPublishView(LoginRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Story
    template_name = 'pump/story_publish_form.html'

    def get_success_url(self):
        return reverse('pump.story.list')


class StoryRemoveView(
        LoginRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Story
    template_name = 'pump/story_remove_form.html'

    def get_success_url(self):
        return reverse('pump.story.list')


class StoryUpdateView(
        LoginRequiredMixin, CheckPermMixin, ContentUpdateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'pump/story_form_wysiwyg.html'

    def get_object(self, *args, **kwargs):
        obj = super(StoryUpdateView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        if not obj.user_can_edit(self.request.user):
            raise PermissionDenied()
        return obj

    def get_success_url(self):
        return self.object.get_absolute_url()
