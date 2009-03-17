from django.core.management.base import NoArgsCommand
from kapsh.tweets.utils import get_tweets

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        get_tweets()
