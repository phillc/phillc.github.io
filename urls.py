from django.conf.urls.defaults import *
from wtflab.apps.blog.models import Entry

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/Users/phillc/Desktop/workspace/wtflab/htdocs/media/'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'', include('wtflab.apps.blog.urls')),
)
