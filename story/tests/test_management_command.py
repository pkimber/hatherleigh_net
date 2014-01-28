from django.test import TestCase

from story.management.commands import demo_data_story
from story.management.commands import init_app_story
from login.management.commands import demo_data_login


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        pre_command = demo_data_login.Command()
        pre_command.handle()
        command = demo_data_story.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_story.Command()
        command.handle()
