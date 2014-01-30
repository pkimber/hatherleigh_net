from django import forms

from bleach import (
    clean,
    ALLOWED_TAGS,
    ALLOWED_ATTRIBUTES,
)
from captcha.fields import CaptchaField

from base.form_utils import (
    RequiredFieldForm,
)

from .models import Story


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
        #attributes = ALLOWED_ATTRIBUTES
        #attributes['img'] = ['align', 'alt', 'src', 'style']
        #styles = ['display', 'height', 'width',]
        #tags = ALLOWED_TAGS + [u'img',]
        attributes = ALLOWED_ATTRIBUTES
        styles = []
        tags = ALLOWED_TAGS + [u'br', u'p',]
        data = clean(data, tags=tags, attributes=attributes, styles=styles)
        return data


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
            'picture': forms.FileInput(attrs=dict(fallback=True)),
        }
