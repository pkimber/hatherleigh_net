from django.core.management.base import BaseCommand

from story.tests.scenario import default_scenario_story


class Command(BaseCommand):

    help = "Create demo data for 'story'"

    def handle(self, *args, **options):
        default_scenario_story()
        print("Created 'story' demo data...")
