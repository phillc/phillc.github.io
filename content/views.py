from models import Entry, Section
from django.shortcuts import get_object_or_404
from django.views.generic import date_based

from models import Section

def section(request, section, template_name='blog/section_archive.html'):
    section_object = get_object_or_404(Section, slug=section)
    return date_based.archive_index(
        request,
        date_field = 'publish',
        queryset = Entry.published.filter(section=section_object),
        template_name = template_name,
        template_object_name = 'entry_list',
        extra_context = {'section': section_object.title},
    )

def section_archive_year(request, sectionSlug, year, template_name = 'blog/section_archive_year.html'):
    section = get_object_or_404(Section, slug=sectionSlug)
    return date_based.archive_year(
        request,
        year = year,
        date_field = 'publish',
        queryset = Entry.published.filter(section=section),
        template_name = template_name,
        extra_context = {'section': section.title},
    )

def section_archive_month(request, sectionSlug, year, month, template_name = 'blog/section_archive_month.html'):
    section = get_object_or_404(Section, slug=sectionSlug)
    return date_based.archive_month(
        request,
        year = year,
        month = month,
        date_field = 'publish',
        queryset = Entry.published.filter(section=section),
        template_name = template_name,
        extra_context = {'section': section.title},
    )

def entry_detail(request, sectionSlug, year, month, day, slug, template_name = 'blog/entry_detail.html', template_object_name='entry'):
    return date_based.object_detail(
        request,
        year = year,
        month = month,
        day = day,
        slug = slug,
        date_field = 'publish',
        queryset = Entry.published.all(),
        template_name = template_name,
        template_object_name = template_object_name
    )


def archive_index(request, template_object_name='entry_list'):
    return date_based.archive_index(
        request,
        date_field = 'publish',
        queryset = Entry.published.all(),
        template_object_name = template_object_name,
    )
