import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from kapsh.content.managers import ContentManager

class Content(models.Model):
    created_by = models.ForeignKey(User, null=True)

    content_type = models.ForeignKey(ContentType,editable=False,null=True)

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    is_published = models.BooleanField(default=False)
    publish = models.DateTimeField(default=datetime.datetime.now)
    publish_end = models.DateTimeField(blank=True, null=True)

    objects = ContentManager()

    class Meta:
        ordering = ['-publish']

    def save(self, force_insert=False, force_update=False):
	if not self.id:
	    self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()

	if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(self.__class__)

	super(Content, self).save(force_insert, force_update)

    def live(self):
        return self in Content.objects.live()
    live.boolean = True

    @property
    def type(self):
	return getattr(self, self.content_type.model)