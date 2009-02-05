from django.db import models
from djangno.utils.translation import ugettext_lazy as _

from content.models import Content
from content.managers import ContentManager

class Entry(Content):
    tease_raw = models.TextField()
    tease_html = models.TextField()

    full_text_raw = models.TextField()
    full_text_html = models.TextField()

    tags = TagField()

    objects = ContentManager()

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
