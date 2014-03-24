# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
    Page,
    Section,
)


PAGE_HOME = 'home'
SECTION_BODY = 'body'


def get_page_home():
    return Page.objects.get(slug=PAGE_HOME)


def get_section_body():
    return Section.objects.get(slug=SECTION_BODY)


class PumpContentModel(ContentModel):

    order = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    site = models.ManyToManyField(Site)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='pump/%Y/%m/%d', blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.user:
            pass
        elif self.email and self.name:
            pass
        else:
            raise ValueError(
                "Story must have a 'user' or a 'name' AND 'email'"
            )
        super(PumpContentModel, self).save(*args, **kwargs)

    def user_can_edit(self, user):
        """
        A member of staff can edit anything.  A standard user can only edit
        their own stories if they haven't been moderated
        """
        result = False
        if user.is_staff:
            result = True
        elif user.is_active and not self.date_moderated:
            result = user == self.user
        return result

    def _author(self):
        return self.name or self.user.username
    author = property(_author)


class EventBlock(BlockModel):
    pass

reversion.register(EventBlock)


class Event(PumpContentModel):
    """Event."""

    block = models.ForeignKey(EventBlock, related_name='content')
    event_date = models.DateField()
    event_time = models.TimeField(help_text='(24 hour clock e.g. 14:30)')

    class Meta:
        ordering = ['modified']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def _get_content_set(self):
        return self.container.event_set

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('pump.event.detail', args=[self.pk])

reversion.register(Event)


class StoryBlock(BlockModel):
    pass

reversion.register(StoryBlock)


class Story(PumpContentModel):
    """News story"""

    block = models.ForeignKey(StoryBlock, related_name='content')
    story_date = models.DateTimeField()

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        ordering = ['-story_date']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def _get_content_set(self):
        return self.container.story_set

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('pump.story.detail', args=[self.pk])

reversion.register(Story)
