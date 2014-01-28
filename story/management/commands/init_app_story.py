from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'story' application"

    def handle(self, *args, **options):
        print "Initialised 'story' app..."
