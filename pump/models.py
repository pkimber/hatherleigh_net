from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from cms.models import (
    ContentModel,
    Section,
)


def get_news_section():
    return Section.objects.get(
        page__slug='home',
        layout__slug='body',
    )


class Area(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __unicode__(self):
        return unicode('{}'.format(self.name))

reversion.register(Area)


class PumpContentModel(ContentModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.ForeignKey(Area)
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


class Event(PumpContentModel):
    """Event."""
    event_date = models.DateField()
    event_time = models.TimeField()

    class Meta:
        ordering = ['modified']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __unicode__(self):
        return unicode('{}'.format(self.title))

reversion.register(Event)


class Story(PumpContentModel):
    """News story"""
    pass

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('container', 'moderate_state')
        ordering = ['-created']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def _get_content_set(self):
        return self.container.story_set

    def __unicode__(self):
        return unicode('{}'.format(self.title))

    def get_absolute_url(self):
        return reverse('pump.story.detail', args=[self.pk])

reversion.register(Story)
