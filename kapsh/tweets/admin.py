from django.contrib import admin
from kapsh.tweets.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet, TweetAdmin)
