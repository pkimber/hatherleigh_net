from django.test import TestCase

from login.tests.scenario import default_scenario_login

from pump.forms import StoryAnonForm
from pump.tests.scenario import (
    default_scenario_pump,
    get_area_hatherleigh,
)


class TestForm(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

    def test_form(self):
        data = dict(
            name='Patrick',
            email='code@pkimber.net',
            area=get_area_hatherleigh().pk,
            title='Chilli Night',
            description='Hot, hot, hot...',
            captcha_0='testing',
            captcha_1='PASSED',
        )
        form = StoryAnonForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEquals(
            'Hot, hot, hot...',
            form.cleaned_data['description']
        )

    def test_form_clean_description_strong(self):
        data = dict(
            name='Patrick',
            email='code@pkimber.net',
            area=get_area_hatherleigh().pk,
            title='Chilli Night',
            description='Hot, <strong>hot</strong>, hot...',
            captcha_0='testing',
            captcha_1='PASSED',
        )
        form = StoryAnonForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEquals(
            'Hot, <strong>hot</strong>, hot...',
            form.cleaned_data['description']
        )
