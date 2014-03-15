# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    get_user_web,
)

from pump.tests.scenario import default_scenario_pump


class TestEventView(TestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_pump()

    def test_create_anon_no_html_editor(self):
        response = self.client.get(reverse('pump.event.create.anon'))
        self.assertNotIn('CKEDITOR', str(response.content))

    def test_pending_order(self):
        pass
