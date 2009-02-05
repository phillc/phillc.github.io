from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

class Section(models.Model):
    """This represents a Section of the website"""
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, prepopulate_from=('title',))
        
    def __unicode__(self):
        return '%s' % self.title
    
class Content(models.Model):

    created_by = models.ForeignKey(User)

    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    section = models.ForeignKey(Section)

    author = models.ForeignKey(Author)

    created = models.DateTimeField(editable=False)
    shown_date = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(editable=False)

    is_published = models.BooleanField(default=True)
    publish_on = models.DateTimeField(default=datetime.now)
    publish_end = models.DateTimeField(blank=True, null=True)

    objects = ContentManager()

    def __unicode__(self):
        return '%s' % self.title

    def save(self):
	if not self.id:
	    self.created = datetime.datetime.now()
	else:
            self.modified = datetime.datetime.now()

 
