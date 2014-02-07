from django.test import TestCase

from login.management.commands import demo_data_login

from pump.management.commands import demo_data_pump
from pump.management.commands import init_app_pump


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        pre_command = demo_data_login.Command()
        pre_command.handle()
        command = demo_data_pump.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_pump.Command()
        command.handle()
