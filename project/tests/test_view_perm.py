# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)

from pump.tests.scenario import (
    default_scenario_pump,
    get_story_market_planning_published,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def test_story_detail(self):
        story = get_story_market_planning_published()
        self.assert_any(
            reverse('project.story.detail', kwargs={'pk': story.block.pk})
        )

    def test_story_archive(self):
        self.assert_any(
            reverse(
                'project.story.archive',
                kwargs=dict(
                    year=date.today().strftime('%Y'),
                    month=date.today().strftime('%b'),
                )
            )
        )
