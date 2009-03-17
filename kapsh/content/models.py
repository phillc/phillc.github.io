import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from content.managers import ContentManager

class Content(models.Model):
    created_by = models.ForeignKey(User, null=True)

    created = models.DateTimeField(editable=False)
    shown_date = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(editable=False)

    is_published = models.BooleanField(default=False)
    publish_on = models.DateTimeField(blank=True, null=True)
    publish_end = models.DateTimeField(blank=True, null=True)

    objects = ContentManager()

    class Meta:
        ordering = ['-shown_date']

    def save(self, force_insert=False, force_update=False):
	if not self.id:
	    self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
	super(Content, self).save(force_insert, force_update)

    def live(self):
        return self in Content.objects.live()
    live.boolean = True
