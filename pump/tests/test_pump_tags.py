# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.test import TestCase

from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
)

from pump.templatetags.pump_tags import (
    event_list,
    story_list,
)
from pump.tests.scenario import (
    default_scenario_pump,
    get_event_garden,
    get_event_history,
    get_event_microchip,
    get_event_temp,
    get_event_temp_today,
    get_story_craft_fair,
    get_story_market_fire,
    get_story_mg_descend,
    get_story_wind_turbines,
)


class TestPumpTags(TestCase):
    """Template tags which return stories and events for the current site."""

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

    def test_event_published_order(self):
        """Make sure template tag shows all events.

        Must include todays events, but not events in the past

        """
        self._publish(get_event_garden())
        self._publish(get_event_history())
        self._publish(get_event_microchip())
        self._publish(get_event_temp())
        self._publish(get_event_temp_today())
        result = event_list()
        published = result.get('event_list')
        self.assertListEqual(
            [
                'Temp Title Today',
                'History Society',
                'Gardening Trip',
            ],
            [t.title for t in published]
        )

    def test_story_published_order(self):
        self._publish(get_story_craft_fair())
        self._publish(get_story_market_fire())
        self._publish(get_story_mg_descend())
        self._publish(get_story_wind_turbines())
        result = story_list()
        published = result.get('story_list')
        self.assertListEqual(
            [
                'Craft Fair',
                'Market Offices burnt down',
                'MGs descend on Hatherleigh',
                'The Market Planning has been Approved',
            ],
            [t.title for t in published]
        )

    def _publish(self, story):
        story.block.publish(get_user_staff())
