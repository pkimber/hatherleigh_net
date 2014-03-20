# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from pump.models import (
    Event,
    EventBlock,
    Story,
    StoryBlock,
)


def make_event_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(EventBlock(**defaults))


def make_event(block, site, **kwargs):
    defaults = dict(
        block=block,
    )
    defaults.update(kwargs)
    event = clean_and_save(Event(**defaults))
    event.site.add(site)
    event.save()
    return event


def make_story_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(StoryBlock(**defaults))


def make_story(block, site, **kwargs):
    defaults = dict(
        block=block,
    )
    defaults.update(kwargs)
    story = clean_and_save(Story(**defaults))
    story.site.add(site)
    story.save()
    return story
