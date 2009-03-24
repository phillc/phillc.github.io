import markdown

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink

from kapsh.content.models import Content
from kapsh.content.managers import ContentManager

from tagging.fields import TagField

class Entry(Content):
    title = models.CharField(_('title'), max_length=64)
    slug = models.SlugField(_('slug'), unique_for_month=True)

    categories = models.ManyToManyField('categories.Category')

    author = models.ForeignKey('authors.Author')

    intro_text_raw = models.TextField(_('Introduction'))
    intro_text_html = models.TextField(editable=False)

    full_text_raw = models.TextField(_('Body Text'))
    full_text_html = models.TextField(editable=False)

    tags = TagField()

    objects = ContentManager()

    def save(self):
        self.intro_text_html = markdown.markdown(self.intro_text_raw)
	self.full_text_html = markdown.markdown(self.full_text_raw)
        super(Entry, self).save()

    @permalink
    def get_absolute_url(self):
        return ('entry_detail', (),
            {
                'year'        : str(self.publish.year),
                'month'       : str(self.publish.strftime('%b')).lower(),
                'day'         : str(self.publish.day).zfill(2),
                'slug'        : str(self.slug),
            },
        )
