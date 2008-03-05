from django.conf.urls.defaults import *
from models import Entry

info_dict = {
    'queryset': Entry.published.all(),
    'date_field': 'publish',
}

#show entire blog by date
urlpatterns = patterns('django.views.generic.date_based',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', info_dict),
    (r'^(?P<year>\d{4})/$', 'archive_year', info_dict),
    (r'^[ ]{0}$', 'archive_index', dict(info_dict, template_object_name='object_list')),
)

#break down to sections
urlpatterns += patterns('blog.views',
    url(r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>[\d]{2})/(?P<slug>[\w-]+)/$', 'entry_detail', name='blog_entry'),
    (r'^(?P<section>[\w-]+)/$', 'section'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month'),
    (r'^(?P<section>[\w-]+)/(?P<year>\d{4})/$', 'archive_year'),
)