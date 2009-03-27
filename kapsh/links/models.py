from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink

class Link(models.Model):
    slug = models.SlugField(_('slug'), unique_for_month=True)
    categories = models.ManyToManyField('categories.Category', blank=True)
    description = models.TextField()
    link = models.URLField()