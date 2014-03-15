# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from pump.models import (
    Area,
    Event,
    Story,
)


def make_area(name, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(name),
    )
    defaults.update(kwargs)
    return clean_and_save(Area(**defaults))


def make_event(container, **kwargs):
    defaults = dict(
        container=container,
    )
    defaults.update(kwargs)
    return clean_and_save(Event(**defaults))


def make_story(container, **kwargs):
    defaults = dict(
        container=container,
    )
    defaults.update(kwargs)
    return clean_and_save(Story(**defaults))
