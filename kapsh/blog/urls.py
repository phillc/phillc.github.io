from django.conf.urls.defaults import *
from kapsh.blog.models import Entry

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>[\d]{2})/(?P<slug>[\w-]+)/$',
        view = 'kapsh.blog.views.entry_detail',
        name='entry_detail',
    ),
)
