from django import template

from pump.models import (
    get_news_section,
    Story,
)

register = template.Library()


@register.inclusion_tag('pump/_story_list.html')
def story_list():
    section = get_news_section()
    return dict(
        story_list=Story.objects.published(section).order_by('-created'),
    )
