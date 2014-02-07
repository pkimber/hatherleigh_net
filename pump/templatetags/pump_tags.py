from django import template

from pump.models import (
    get_section_story,
    Story,
)

register = template.Library()


@register.inclusion_tag('pump/_story_list.html')
def story_list():
    section = get_section_story()
    return dict(
        story_list=Story.objects.published(section).order_by('-created'),
    )
