from django import template

from pump.models import (
    get_section_event,
    get_section_story,
    Event,
    Story,
)

register = template.Library()


@register.inclusion_tag('pump/_event_list.html')
def event_list():
    section = get_section_event()
    return dict(
        event_list=Event.objects.published(section).order_by(
            'event_date', 'event_time'
        ),
    )


@register.inclusion_tag('pump/_story_list.html')
def story_list():
    section = get_section_story()
    return dict(
        story_list=Story.objects.published(section).order_by('-created'),
    )
