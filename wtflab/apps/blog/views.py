from models import Entry, Section
from django.shortcuts import get_object_or_404
from django.views.generic import date_based

def section(request, section):
    sectiono = get_object_or_404(Section, slug=section)
    return date_based.archive_index(
        request,
        date_field = 'publish',
        queryset = Entry.published.filter(section=sectiono),
        template_name = 'blog/section_archive.html',
        template_object_name = 'object_list',
        extra_context = {'section': sectiono.title},
    )

def archive_year(request, section, year):
    sectiono = get_object_or_404(Section, slug=section)
    return date_based.archive_year(
        request,
        year = year,
        date_field = 'publish',
        queryset = Entry.published.filter(section=sectiono),
        template_name = 'blog/section_archive_year.html',
        extra_context = {'section': sectiono.title},
    )

def archive_month(request, section, year, month):
    sectiono = get_object_or_404(Section, slug=section)
    return date_based.archive_month(
        request,
        year = year,
        month = month,
        date_field = 'publish',
        queryset = Entry.published.filter(section=sectiono),
        template_name = 'blog/section_archive_month.html',
        extra_context = {'section': sectiono.title},
    )