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

        photo_info = flickr.photos_getInfo(photo_id=uid)
        posted_at = datetime.datetime.fromtimestamp(int(photo_info.find('photo').find('dates').attrib['posted']))
        url = photo_info.find('photo').find('urls')[0].text

        p, created = Photo.objects.get_or_create(
            uid = uid,
            defaults = {
                'server': server,
                'farm': farm,
                'secret': secret,
                'is_published': True,
                'publish': posted_at,
            }
        )
        p.title = title
        p.url = url
        p.save()
