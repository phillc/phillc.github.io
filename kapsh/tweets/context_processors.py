from django.conf import settings
 
def twitter_user(request):
    return {'TWITTER_USER': settings.TWITTER_USER}
