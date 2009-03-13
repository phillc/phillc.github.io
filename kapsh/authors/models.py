from django.db import models
from django.utils.translation import ugettext_lazy as _

class Author(models.Model):
    first_name = models.CharField(_('First Name'), max_length=64)
    last_name = models.CharField(_('Last Name'), max_length=64)
    middle = models.CharField(_('Middle'), max_length=32)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

