import datetime

from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet

class ContentQuerySet(QuerySet):
    def category(self, category):
        return self.filter(
            Q(category=category)
        )

class ContentManager(models.Manager):
    def get_query_set(self):
	return ContentQuerySet(self.model)

    def live(self):
        queryset = self.all()
        now = datetime.datetime.now()
        return queryset.filter(
            Q(is_published=True),
            Q(publish__lte=now),
            Q(publish_end__gte=now) | Q(publish_end__isnull=True),
        )
