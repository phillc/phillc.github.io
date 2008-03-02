from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from wtflab.apps.blog.managers import PublishedManager
from tagging.fields import TagField

class Section(models.Model):
    """This represents a Section of the website"""
    title = models.CharField(max_length=64)
    slug = models.SlugField(prepopulate_from=('title',), unique=True)
    
    class Admin:
        list_display = ('title', 'slug')
        
    def __unicode__(self):
        return '%s' % self.title

class Entry(models.Model):
    """This is everything on the web site except the videos.... and maybe pictures"""
    
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
        (3, 'Closed'),
    )

    title     = models.CharField(max_length=64)
    slug      = models.SlugField(prepopulate_from=('title',), unique_for_date='publish')
    author    = models.ForeignKey(User, blank=True, null=True)
    tease     = models.TextField(blank=True)
    body      = models.TextField()
    status    = models.IntegerField(choices=STATUS_CHOICES, radio_admin=True, default=1)
    publish   = models.DateTimeField(default=datetime.now)
    created   = models.DateTimeField(auto_now_add=True)
    modified  = models.DateTimeField(auto_now=True)
    section   = models.ForeignKey(Section)
    tags      = TagField()
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        verbose_name_plural = "Entries"
    
    class Admin:
        list_display = ('title', 'publish')
        list_filter   = ('publish', 'section', 'status', 'author')
        ordering = ('-publish',)
        search_fields = ('title', 'body')
    
    def __unicode__(self):
        return '%s' % self.title