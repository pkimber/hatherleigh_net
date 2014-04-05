# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django import template
from django.contrib.sites.models import Site

from pump.models import (
    Event,
    get_home_body,
    Story,
)

register = template.Library()


@register.inclusion_tag('_event_list.html')
def event_list():
    """List of events.

    The '_event_list.html' template can be found in the ftp folder.

    """
    current_site = Site.objects.get_current()
    home_body = get_home_body()
    return dict(
        event_list=Event.objects.published(
            home_body,
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
    home_body = get_home_body()
    return dict(
        story_list=Story.objects.published(
            home_body,
        ).filter(
            site__id__exact=current_site.pk,
        ).order_by(
            '-story_date'
        ),
    )
