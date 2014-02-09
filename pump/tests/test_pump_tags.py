from django.test import TestCase

from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
)

from pump.templatetags.pump_tags import story_list
from pump.tests.scenario import (
    default_scenario_pump,
    get_story_craft_fair,
    get_story_market_fire,
    get_story_mg_descend,
)


class TestPumpTags(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

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
