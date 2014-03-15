# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)

from pump.tests.scenario import default_scenario_pump

class TestViewOtherPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def test_home(self):
        self.assert_logged_in(reverse('pump.dashboard'))
