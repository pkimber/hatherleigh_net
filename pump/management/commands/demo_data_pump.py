# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from pump.tests.scenario import default_scenario_pump


class Command(BaseCommand):

    help = "Create demo data for 'pump'"

    def handle(self, *args, **options):
        default_scenario_pump()
        print("Created 'pump' demo data...")
