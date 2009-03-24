from django.conf import settings

def disqus_forum(request):
    return {'DISQUS_FORUM': settings.DISQUS_FORUM}
