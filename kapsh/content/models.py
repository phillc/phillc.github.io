import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from content.managers import ContentManager

class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_month=True)
        
    def __unicode__(self):
        return '%s' % self.title
    
class Author(models.Model):
    first_name = models.CharField(_('First Name'), max_length=64)
    last_name = models.CharField(_('Last Name'), max_length=64)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Content(models.Model):
    created_by = models.ForeignKey(User)

    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    categories = models.ManyToManyField(Category)

    author = models.ForeignKey(Author)

    created = models.DateTimeField(editable=False)
    shown_date = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(editable=False)

    is_published = models.BooleanField(default=True)
    publish_on = models.DateTimeField(default=datetime.datetime.now)
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