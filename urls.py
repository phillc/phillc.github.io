from django.conf.urls.defaults import *
from beerthree.settings import DEBUG

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^google9eee2da00290540a.html$', 'blog.views.section', {'section': 'wtf'}),
    (r'', include('blog.urls')),
)

if DEBUG:
    from settings import MEDIA_ROOT
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
