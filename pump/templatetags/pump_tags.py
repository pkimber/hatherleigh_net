# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from datetime import date

from django import template

from pump.models import (
    get_page_home,
    get_section_body,
    Event,
    Story,
)

register = template.Library()


@register.inclusion_tag('pump/_event_list.html')
def event_list():
    page = get_page_home()
    section = get_section_body()
    return dict(
        event_list=Event.objects.published(
            page,
            section,
        ).filter(
            event_date__gte=date.today()
        ).order_by(
            'event_date',
            'event_time',
        ),
    )


@register.inclusion_tag('pump/_story_list.html')
def story_list():
    page = get_page_home()
    section = get_section_body()
    return dict(
        story_list=Story.objects.published(
            page,
            section,
        ).order_by(
            '-created'
        ),
    )
