from django.conf.urls.defaults import *
from models import Entry

info_dict = {
    'queryset': Entry.published.all(),
    'date_field': 'publish',
}

#show entire blog by date
urlpatterns = patterns('django.views.generic.date_based',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', info_dict),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', info_dict),
    (r'^(?P<year>\d{4})/$', 'archive_year', info_dict),
    (r'^[ ]{0}$', 'archive_index', info_dict),
)

#break down to sections
urlpatterns += patterns('wtflab.apps.blog.views',
    (r'^(?P<section>[\w-]+)/$', 'section'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>\w+)/$', 'entry_detail'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<week>\w{1,2})/$', 'archive_week'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/$', 'archive_year'),
)