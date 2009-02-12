from django.conf.urls.defaults import *
from kapsh.settings import DEBUG, DEV_SERVER, MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^$', 'kapsh.homepage.views.home', name='home'),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
)

if DEBUG and DEV_SERVER:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
