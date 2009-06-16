import datetime
import twitter
from django.conf import settings
from kapsh.tweets.models import Tweet
import pytz

def get_tweets():
    tz = pytz.timezone('US/Eastern')
    utc = pytz.timezone('UTC')

    api = twitter.Api()
    tweet_list = api.GetUserTimeline(settings.TWITTER_USER)

    for tweet in tweet_list:
        date_utc = datetime.datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=utc)
        tweet.date = date_utc.astimezone(tz).replace(tzinfo=None)
        Tweet.objects.get_or_create(
            uid = "%s" % (tweet.id),
    	    defaults = {
                'text_raw': tweet.text,
                'publish': tweet.date,
                'is_published': True,
            }
        )
