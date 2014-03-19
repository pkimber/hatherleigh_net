# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from pump.models import (
    Area,
    Event,
    EventBlock,
    Story,
    StoryBlock,
)


def make_area(name, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(name),
    )
    defaults.update(kwargs)
    return clean_and_save(Area(**defaults))


def make_event_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(EventBlock(**defaults))


def make_event(block, **kwargs):
    defaults = dict(
        block=block,
    )
    defaults.update(kwargs)
    return clean_and_save(Event(**defaults))


def make_story_block(page, section, **kwargs):
    defaults = dict(
        page=page,
        section=section,
    )
    defaults.update(kwargs)
    return clean_and_save(StoryBlock(**defaults))


def make_story(block, **kwargs):
    defaults = dict(
        block=block,
    )
    defaults.update(kwargs)
    return clean_and_save(Story(**defaults))
