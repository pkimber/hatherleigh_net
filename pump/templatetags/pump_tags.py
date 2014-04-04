# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django import template
from django.contrib.sites.models import Site

from pump.models import (
    get_page_home,
    get_section_body,
    Event,
    Story,
)

register = template.Library()


@register.inclusion_tag('_event_list.html')
def event_list():
    """List of events.

    The '_event_list.html' template can be found in the ftp folder.

    """
    current_site = Site.objects.get_current()
    page = get_page_home()
    section = get_section_body()
    return dict(
        event_list=Event.objects.published(
            page,
            section,
        ).filter(
            event_date__gte=date.today(),
            site__id__exact=current_site.pk,
        ).order_by(
            'event_date',
            'event_time',
        ),
    )


@register.inclusion_tag('_story_list.html')
def story_list():
    """List of stories.

    The '_story_list.html' template can be found in the ftp folder.

    """
    current_site = Site.objects.get_current()
    page = get_page_home()
    section = get_section_body()
    return dict(
        story_list=Story.objects.published(
            page,
            section,
        ).filter(
            site__id__exact=current_site.pk,
        ).order_by(
            '-story_date'
        ),
    )
