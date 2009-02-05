from django.db import models
from django.db.models import Q

class ContentManager(models.Manager):
    def live(self):
        queryset = self.all()
        now = datetime.datetime.now()
        return queryset.filter(
            Q(is_published=True),
            Q(start_publish_date__lte=now) | Q(start_publish_date__isnull=True),
            Q(end_publish_date__gte=now) | Q(end_publish_date__isnull=True),
        )
