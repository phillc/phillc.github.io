from django.conf.urls.defaults import *
from django.contrib import admin
from kapsh.settings import DEBUG, DEV_SERVER, MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'kapsh.homepage.views.home', name='home'),
    ('^admin/', include(admin.site.urls)),
)

if DEBUG and DEV_SERVER:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
