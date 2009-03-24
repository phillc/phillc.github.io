from kapsh.content.models import Content

from django.db import models

class Tweet(Content):
    uid = models.IntegerField()
    text_raw = models.TextField()
    text_html = models.TextField()

    def save(self, force_insert=False, force_update=False):
	self.text_html = self.text_raw
	super(Tweet, self).save(force_insert, force_update)