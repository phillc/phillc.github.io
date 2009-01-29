from blog.models import Entry
from django.template import Node, Library

register = Library()

class LatestEntriesNode(Node):
    def __init__(self, number_grabbed, var_name):
        self.number_grabbed = number_grabbed
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = Entry.published.all()[:self.number_grabbed]
        return ''

def get_latest_entries(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError, "get_latest_entries takes 3 arguments"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "second argument to get_latest_entries tag must be 'as'"
    return LatestEntriesNode(bits[1], bits[3])
    
get_latest_entries = register.tag(get_latest_entries)
