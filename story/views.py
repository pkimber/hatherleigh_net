from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from cms.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import (
    StoryAnonForm,
    StoryEmptyForm,
    StoryTrustForm,
)
from .models import (
    get_news_section,
    Story,
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


class StoryAnonCreateView(ContentCreateView):

    form_class = StoryAnonForm
    model = Story
    template_name = 'story/story_create_form.html'

    def get(self, request, *args, **kwargs):
        """
        If a user is logged in (and active), they shouldn't be using this
        view... they can use the view for a logged in user.
        """
        if self.request.user and self.request.user.is_active:
            return HttpResponseRedirect(reverse('story.create.trust'))
        else:
            return super(StoryAnonCreateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project.home')


class StoryTrustCreateView(
        LoginRequiredMixin, ContentCreateView):

    form_class = StoryTrustForm
    model = Story
    template_name = 'story/story_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(StoryTrustCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('story.list')


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
    template_name = 'story/story_list.html'

    def get_queryset(self):
        section = get_news_section()
        if self.request.user.is_staff:
            result = Story.objects.pending(section)
        else:
            result = Story.objects.pending(
                section,
                dict(user=self.request.user)
            )
        return result


class StoryPublishView(LoginRequiredMixin, ContentPublishView):

    form_class = StoryEmptyForm
    model = Story
    template_name = 'story/story_publish_form.html'

    def get_success_url(self):
        return reverse('story.list')


class StoryRemoveView(
        LoginRequiredMixin, ContentRemoveView):

    form_class = StoryEmptyForm
    model = Story
    template_name = 'story/story_remove_form.html'

    def get_success_url(self):
        return reverse('story.list')


class StoryUpdateView(
        LoginRequiredMixin, CheckPermMixin, ContentUpdateView):

    model = Story
    form_class = StoryTrustForm
    template_name = 'story/story_update_form.html'

    def get_object(self, *args, **kwargs):
        obj = super(StoryUpdateView, self).get_object(*args, **kwargs)
        self._check_perm(obj)
        if not obj.user_can_edit(self.request.user):
            raise PermissionDenied()
        return obj

    def get_success_url(self):
        return reverse('story.list')
