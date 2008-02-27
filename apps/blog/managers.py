from django.db.models import Manager
from datetime import datetime

class PublishedManager(Manager):
    def get_query_set(self):
        queryset = super(PublishedManager, self).get_query_set()
        return queryset.filter(status=2, publish__lte=datetime.now)