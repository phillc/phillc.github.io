from django.conf.urls.defaults import *
from blog.models import Entry

urlpatterns = patterns('blog.views',
    url(r'^(?P<sectionSlug>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>[\d]{2})/(?P<slug>[\w-]+)/$',
        view = 'entry_detail',
        name='blog_entry',
    ),
    url(r'^(?P<section>[\w-]+)/$',
        view = 'section',
        name = 'section',
    ),
    url(r'^(?P<section>[\w-]+)/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        view = 'section_archive_month',
        name = 'section_archive_month',
    ),
    url(r'^(?P<section>[\w-]+)/(?P<year>\d{4})/$',
        view = 'section_archive_year',
        name = 'section_archive_year',
    ),
#     url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
#         view   = 'archive_month',
#         name   = 'archive_month',
#     ),
#     url(r'^(?P<year>\d{4})/$',
#         view   = 'archive_year',
#         name   = 'archive_year',
#     ),
    url(
        regex = '^$',
        view   = 'archive_index',
        name   = 'home',
    )
)
