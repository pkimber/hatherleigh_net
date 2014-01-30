from django.core.urlresolvers import reverse
from django.test import TestCase

from base.tests.test_utils import PermTestCase
from story.models import Story
from story.tests.scenario import default_scenario_story
from login.tests.scenario import (
    default_scenario_login,
    get_user_web,
)


class TestView(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_story()

    def test_create_trust_html_editor(self):
        web = get_user_web()
        self.client.login(username=web.username, password=web.username)
        response = self.client.get(reverse('story.create.trust'))
        self.assertIn('CKEDITOR', response.content)

    def test_create_anon_no_html_editor(self):
        response = self.client.get(reverse('story.create.anon'))
        self.assertNotIn('CKEDITOR', response.content)
