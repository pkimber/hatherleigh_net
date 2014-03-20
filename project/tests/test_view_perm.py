# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)

from pump.tests.scenario import (
    default_scenario_pump,
    get_site_hatherleigh,
    get_story_market_planning,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def test_detail_perm(self):
        story = get_story_market_planning()
        self.assert_any(
            reverse('project.story.detail', kwargs={'pk': story.block.pk})
        )
