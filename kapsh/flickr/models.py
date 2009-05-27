from kapsh.content.models import Content

from django.db import models

class Photo(Content):
    uid = models.CharField(max_length="64", unique=True)
    title = models.CharField(max_length=128)
    server = models.CharField(max_length=16)
    farm = models.CharField(max_length=8)
    secret = models.CharField(max_length=16)

    def __unicode__(self):
        return 'http://farm' + self.farm + '.static.flickr.com/' + self.server+ '/' + self.uid + '_' + self.secret + '.jpg'
