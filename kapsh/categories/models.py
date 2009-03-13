from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_month=True)

    def __unicode__(self):
        return '%s' % self.title
