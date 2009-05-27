import datetime
import flickrapi
from django.conf import settings
from kapsh.flickr.models import Photo


def get_photos():
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY)
    my_photos = flickr.people_GetPublicPhotos(user_id='7932291@N02')
    photos_element = my_photos.find('photos')
    for photo in photos_element:
        server = photo.attrib['server']
        title = photo.attrib['title']
        uid = photo.attrib['id']
        farm = photo.attrib['farm']
        secret = photo.attrib['secret']
        Photo.objects.get_or_create(
            uid = uid,
            defaults = {
                'server': server,
                'title': title,
                'farm': farm,
                'secret': secret,
                'is_published': True,
                'publish': datetime.datetime.now()
            }
        )
