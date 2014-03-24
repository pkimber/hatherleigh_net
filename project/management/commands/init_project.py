# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from django.core.management.base import BaseCommand

from block.tests.scenario import default_block_state
from pump.tests.scenario import (
    default_section,
    default_site,
)


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        default_section()
        default_block_state()
        default_site()
        print("Project initialised...")
