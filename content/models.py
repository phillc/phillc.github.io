from datetime import datetime
from time import strftime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import permalink
from django.core.urlresolvers import reverse

from blog.managers import PublishedManager

from tagging.fields import TagField


class Section(models.Model):
    """This represents a Section of the website"""
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, prepopulate_from=('title',))
        
    def __unicode__(self):
        return '%s' % self.title
    
class Author(models.Model):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
        (3, 'Closed'),
    )

    created_by = models.ForeignKey(User)

    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    author           = models.ForeignKey(Author)

    status           = models.IntegerField(choices=STATUS_CHOICES, radio_admin=True, default=1)
    publish          = models.DateTimeField(default=datetime.now)
    created          = models.DateTimeField(auto_now_add=True)
    modified         = models.DateTimeField(auto_now=True)
    section          = models.ForeignKey(Section)
    tags             = TagField()
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-publish']
        
    def __unicode__(self):
        return '%s' % self.title
    
    def save(self):
        if self.render_method == 'markdown':
            import markdown
            renderer = markdown.markdown
        elif self.render_method == 'textile':
            import textile
            renderer = textile.textile
        self.tease = renderer(self.tease_markdown)
        self.body  = renderer(self.body_markdown)
        super(Entry, self).save()

    def get_author_display_name(self):
        name = ''
        try:
            author = self.author
        except User.DoesNotExist:
            return False
        if author.first_name and author.last_name:
            name = '%s %s' % (author.first_name, author.last_name)
        elif author.first_name:
            name = '%s' % (author.first_name)
        else:
            name = author.username
        return name
        

    
    @permalink
    def get_absolute_url(self):
        return ('blog_entry', (),
            {
                'sectionSlug' : str(self.section.slug),
                'year'        : str(self.publish.year),
                'month'       : str(self.publish.strftime('%b')).lower(),
                'day'         : str(self.publish.day).zfill(2),
                'slug'        : str(self.slug),
            },
        )
        
