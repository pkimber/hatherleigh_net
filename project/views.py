from django.views.generic import TemplateView

from story.models import Story


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(dict(
            #story_list=Story.objects.filter(date_moderated__isnull=False),
            story_list=Story.objects.all(),
        ))
        return context


class SecureView(TemplateView):
    template_name = 'project/secure.html'
