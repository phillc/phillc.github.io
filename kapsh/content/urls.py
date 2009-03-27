from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^$',
	view='kapsh.content.views.archive',
	name='content_archive',
    ),
    url(
        r'^page/(?P<page>\d+)/$',
        view='kapsh.content.views.archive',
        name='content_archive_page',
    ),
)
