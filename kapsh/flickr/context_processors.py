from django.conf import settings
 
def flickr_user(request):
    return {'FLICKR_USER': settings.FLICKR_USER}
