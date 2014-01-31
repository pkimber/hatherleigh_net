from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView,
    TemplateView,
)

from cms.models import (
    Container,
)
from story.models import (
    get_news_section,
    Story,
)


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        section = get_news_section()
        context.update(dict(
            story_list=Story.objects.published(section).order_by('-created'),
        ))
        return context


class NewsDetailView(DetailView):

    model = Container
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        story = get_object_or_404(
            self.object.story_set,
            moderate_state__slug='published'
        )
        context.update(dict(
            story=story,
        ))
        return context


class SecureView(TemplateView):

    template_name = 'project/secure.html'
