# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from captcha.fields import CaptchaField

from base.form_utils import (
    bleach_clean,
    RequiredFieldForm,
)

from .models import (
    Event,
    Story,
)


class EventEmptyForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ()


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
            'area',
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
            'area',
            'event_date',
            'event_time',
            'title',
            'description',
            'picture',
        )
        widgets = {
            'picture': forms.FileInput,
        }

class StoryEmptyForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ()


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
        fields = ('name', 'email', 'area', 'title', 'description', 'picture')
        widgets = {
            'picture': forms.FileInput,
        }


class StoryTrustForm(StoryForm):

    class Meta:
        model = Story
        fields = ('area', 'title', 'description', 'picture')
        widgets = {
            'picture': forms.FileInput,
        }
