from django.views.generic import list_detail
from kapsh.content.models import Content

def home(request):
    content_list = Content.objects.live()
    return list_detail.object_list(
        request,
	queryset=content_list,
	paginate_by=10,
        template_object_name='content',
        template_name='homepage/home.html',
        extra_context={
            'page_id': 'home',
        },
    )