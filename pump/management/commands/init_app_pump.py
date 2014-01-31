from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'pump' application"

    def handle(self, *args, **options):
        print "Initialised 'pump' app..."
