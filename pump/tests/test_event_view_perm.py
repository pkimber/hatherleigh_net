from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)

from pump.models import Story
from pump.tests.scenario import (
    default_scenario_pump,
    get_area_hatherleigh,
    get_story_craft_fair,
    get_story_market_fire,
)


class TestEventViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def test_create_anon(self):
        self.assert_any(reverse('pump.event.create.anon'))
