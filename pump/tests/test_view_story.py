from django.core.urlresolvers import reverse
from django.test import TestCase

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
)

from pump.models import (
    get_section_story,
    Story,
)
from pump.templatetags.pump_tags import story_list
from pump.tests.scenario import (
    default_scenario_pump,
    get_story_craft_fair,
    get_story_market_fire,
    get_story_mg_descend,
)


class TestViewStory(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

    def test_create_trust_html_editor(self):
        web = get_user_web()
        self.client.login(username=web.username, password=web.username)
        response = self.client.get(reverse('pump.story.create.trust'))
        self.assertIn('CKEDITOR', response.content)

    def test_create_anon_no_html_editor(self):
        response = self.client.get(reverse('pump.story.create.anon'))
        self.assertNotIn('CKEDITOR', response.content)

    def test_pending_order(self):
        user = get_user_staff()
        self.client.login(username=user.username, password=user.username)
        response = self.client.get(reverse('pump.story.list'))
        pending = response.context_data['story_list']
        self.assertListEqual(
            [
                'Craft Fair',
                'Market Offices burnt down',
                'MGs descend on Hatherleigh',
            ],
            [t.title for t in pending]
        )

    def test_published_order(self):
        self._publish(get_story_craft_fair())
        self._publish(get_story_market_fire())
        self._publish(get_story_mg_descend())
        result = story_list()
        published = result.get('story_list')
        self.assertListEqual(
            [
                'Craft Fair',
                'Market Offices burnt down',
                'MGs descend on Hatherleigh',
            ],
            [t.title for t in published]
        )

    def _publish(self, story):
        story.set_published(get_user_staff())
        story.save()
