from django.conf.urls.defaults import *
from django.contrib import admin
from kapsh.settings import DEBUG, DEV_SERVER, MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'kapsh.content.views.archive', name='home'),
    ('^', include('kapsh.content.urls')),
    ('^blog/', include('kapsh.blog.urls')),
    ('^admin/', include(admin.site.urls)),
)

if DEBUG and DEV_SERVER:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
