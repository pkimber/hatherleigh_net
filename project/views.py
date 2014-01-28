from django.views.generic import TemplateView

from cms.models import Section
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


class SecureView(TemplateView):

    template_name = 'project/secure.html'
