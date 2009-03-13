import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from content.managers import ContentManager

class Content(models.Model):
    created_by = models.ForeignKey(User)

    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    categories = models.ManyToManyField('categories.Category')

    author = models.ForeignKey('authors.Author')

    created = models.DateTimeField(editable=False)
    shown_date = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(editable=False)

    is_published = models.BooleanField(default=False)
    publish_on = models.DateTimeField(blank=True, null=True)
    publish_end = models.DateTimeField(blank=True, null=True)

    objects = ContentManager()

    class Meta:
        ordering = ['-shown_date']

    def __unicode__(self):
        return '%s' % self.title

    def save(self):
	if not self.id:
	    self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
	super(Content, self).save()

    def live(self):
        return self in Content.objects.live()
    live.boolean = True
