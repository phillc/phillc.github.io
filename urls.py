from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/Users/phillc/Desktop/workspace/wtflab.com/media/'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^google9eee2da00290540a.html$', 'blog.views.section', {'section': 'wtf'}),
    (r'', include('blog.urls')),
)