from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/Users/phillc/Desktop/workspace/wtflab.com/media/'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'', include('blog.urls')),
)
