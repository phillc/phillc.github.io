import datetime
import twitter
from django.conf import settings
from kapsh.tweets.models import Tweet

def get_tweets():
    api = twitter.Api()
    tweet_list = api.GetUserTimeline(settings.TWITTER_USER)

    for tweet in tweet_list:
	tweet.date = datetime.datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y")
        Tweet.objects.get_or_create(
            uid = tweet.id,
    	    defaults = {
                'text': tweet.text,
                'shown_date': tweet.date,
                'is_published': True,
            }
        )