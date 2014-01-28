from django import forms

from captcha.fields import CaptchaField

from base.form_utils import (
    RequiredFieldForm,
)

from .models import Story


class StoryEmptyForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ()


class StoryAnonForm(RequiredFieldForm):
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
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = Story
        fields = ('name', 'email', 'area', 'title', 'description', 'picture')


class StoryTrustForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(StoryTrustForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = Story
        fields = ('area', 'title', 'description', 'picture')
