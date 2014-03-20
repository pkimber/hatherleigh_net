# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
)

from pump.tests.scenario import default_scenario_pump


class TestViewStory(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

    def test_create_trust_html_editor(self):
        web = get_user_web()
        self.client.login(username=web.username, password=web.username)
        response = self.client.get(reverse('pump.story.create.trust'))
        self.assertIn('CKEDITOR', str(response.content))

    def test_create_anon_no_html_editor(self):
        response = self.client.get(reverse('pump.story.create.anon'))
        self.assertNotIn('CKEDITOR', str(response.content))

    def test_pending_order(self):
        user = get_user_staff()
        self.client.login(username=user.username, password=user.username)
        response = self.client.get(reverse('pump.story.list'))
        pending = response.context_data['story_list']
        self.assertListEqual(
            [
                'The Market Planning has been Approved',
                'Craft Fair',
                'Market Offices burnt down',
                'MGs descend on Hatherleigh',
            ],
            [t.title for t in pending]
        )
