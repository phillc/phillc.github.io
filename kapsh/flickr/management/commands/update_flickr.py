from django.core.management.base import NoArgsCommand
from kapsh.flickr.utils import get_flickr

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        get_flickr()
