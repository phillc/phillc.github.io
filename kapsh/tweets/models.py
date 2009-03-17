from kapsh.content.models import Content

from django.db import models

class Tweet(Content):
    uid = models.IntegerField()
    text = models.TextField()