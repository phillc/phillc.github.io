from django.views.generic.simple import direct_to_template
from content.models import Content

def home(request):
    content_list = Content.objects.live()
    return direct_to_template(request,
        'homepage/home.html',
        {
            'page_id': 'home',
            'content_list': content_list,
        })