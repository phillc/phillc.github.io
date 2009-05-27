from django.core.management.base import NoArgsCommand
from kapsh.flickr.utils import get_photos

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        get_photos()
