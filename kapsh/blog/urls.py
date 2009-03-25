from django.conf.urls.defaults import *
from kapsh.blog.models import Entry

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>[\d]{2})/(?P<slug>[\w-]+)/$',
        view = 'entry_detail',
        name='entry_detail',
    ),
)
