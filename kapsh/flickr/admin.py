from django.contrib import admin
from kapsh.flickr.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
