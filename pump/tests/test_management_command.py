# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from login.management.commands import demo_data_login

from pump.management.commands import demo_data_pump


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        pre_command = demo_data_login.Command()
        pre_command.handle()
        command = demo_data_pump.Command()
        command.handle()
