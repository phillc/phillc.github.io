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
        
    class Admin:
        list_display = ('title', 'slug')
        
    def __unicode__(self):
        return '%s' % self.title
    
#class SectionOptions(admin.ModelAdmin):
#    list_display = ('title', 'slug')
#    prepopulated_fields = {'slug': ('title',)}
#    
#admin.site.register(Section, SectionOptions)

class Entry(models.Model):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public'),
        (3, 'Closed'),
    )

    RENDER_METHODS = (
        ('markdown', 'Markdown'),
        ('textile', 'Textile')
    )

    created_by = models.ForeignKey(User)

    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    author           = models.ForeignKey(User)

    tease_markdown   = models.TextField()
    tease            = models.TextField(editable=False)
    body_markdown    = models.TextField()
    body             = models.TextField(editable=False)
    status           = models.IntegerField(choices=STATUS_CHOICES, radio_admin=True, default=1)
    publish          = models.DateTimeField(default=datetime.now)
    created          = models.DateTimeField(auto_now_add=True)
    modified         = models.DateTimeField(auto_now=True)
    section          = models.ForeignKey(Section)
    comments_enabled = models.BooleanField(default=True)
    render_method    = models.CharField(max_length=15, choices=RENDER_METHODS, default=RENDER_METHODS[0][0])
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
        
#class EntryOptions(admin.ModelAdmin):
#    list_display = ('title', 'status')
#    list_filter   = ('publish', 'section', 'status', 'author')
#    ordering = ('-publish',)
#    search_fields = ('title', 'body')
#    prepopulated_fields = {'slug': ('title',)}
#    
#admin.site.register(Entry, EntryOptions)

class EntryModerator(CommentModerator):
    akismet = True
    enable_field = 'comments_enabled'
    
moderator.register(Entry, EntryModerator)
    
