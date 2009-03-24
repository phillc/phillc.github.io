from django.views.generic import date_based

from kapsh.blog.models import Entry

def entry_detail(request, year, month, day, slug,):
    return date_based.object_detail(
        request,
        year = year,
        month = month,
        day = day,
        slug = slug,
        date_field = 'publish',
        template_object_name = 'entry',
        queryset = Entry.objects.all(),
    )