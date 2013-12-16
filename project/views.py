from django.views.generic import TemplateView

from story.models import Story


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(dict(
            story_list=Story.objects.filter(
                moderate_state__slug='published'
            ).order_by('-created'),
        ))
        return context


class SecureView(TemplateView):
    template_name = 'project/secure.html'
