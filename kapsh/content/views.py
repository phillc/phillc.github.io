from django.views.generic import list_detail
from django.core.urlresolvers import reverse
from kapsh.content.models import Content

def archive(request, page=1):
    content_list = Content.objects.live()
    return list_detail.object_list(
        request,
	queryset=content_list,
	paginate_by=20,
        page=page,
        template_object_name='content',
        template_name='content/home.html',
        extra_context={
            'page_id': 'home',
            'base_url': reverse('content_archive'),
        },
    )