# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.sites.models import Site

from captcha.fields import CaptchaField

from base.form_utils import (
    bleach_clean,
    RequiredFieldForm,
)

from .models import (
    Event,
    Story,
)


class SiteNameModelChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return '{}'.format(obj.name)


class EventForm(RequiredFieldForm):
    """This is an 'abstract' base class, designed to inherited."""

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['site'] = SiteNameModelChoiceField(
            queryset=Site.objects.all().order_by('name')
        )

    def clean_description(self):
        data = self.cleaned_data['description']
        return bleach_clean(data)


class EventAnonForm(EventForm):
    """user is not logged in... so we need a captcha"""
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(EventAnonForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['name'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )

    class Meta:
        model = Event
        fields = (
            'name',
            'email',
            'site',
            'event_date',
            'event_time',
            'title',
            'description',
            'picture'
        )
        widgets = {
            'picture': forms.FileInput,
        }


class EventTrustForm(EventForm):

    class Meta:
        model = Event
        fields = (
            'site',
            'event_date',
            'event_time',
            'title',
            'description',
            'picture',
        )
        widgets = {
            'picture': forms.FileInput,
        }


class StoryForm(RequiredFieldForm):
    """This is an 'abstract' base class, designed to inherited."""

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['site'] = SiteNameModelChoiceField(
            queryset=Site.objects.all().order_by('name')
        )

    def clean_description(self):
        data = self.cleaned_data['description']
        return bleach_clean(data)


class StoryAnonForm(StoryForm):
    """user is not logged in... so we need a captcha"""
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(StoryAnonForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
        self.fields['name'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'pure-input-1-2'}
        )

    class Meta:
        model = Story
        fields = ('name', 'email', 'site', 'title', 'description', 'picture')
        widgets = {
            'picture': forms.FileInput,
        }


class StoryTrustForm(StoryForm):

    class Meta:
        model = Story
        fields = ('site', 'title', 'description', 'picture')
        widgets = {
            'picture': forms.FileInput,
        }
