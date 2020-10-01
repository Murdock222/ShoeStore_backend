from django.core.management.base import BaseCommand, CommandError
from api import models
class Command(BaseCommand):
    help = 'populate the shoetype'


    def handle(self, *args, **options):
        return models.Shoe.objects.Populatedata()