# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from project.management.commands import init_project


class TestCommand(TestCase):

    def test_init_projec(self):
        """ Test the management command """
        command = init_project.Command()
        command.handle()
