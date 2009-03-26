from django import template

register = template.Library()

class FullContentNode(template.Node):
    def __init__(self, content, template_type):
        self.content = template.Variable(content)
        self.template_type = template_type

    def render(self, context):
        try:
            content_obj = self.content.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        c_type = content_obj.type
        opt = c_type._meta
        template_location = '%s/_%s_%s.html' % (opt.app_label, opt.object_name.lower(), self.template_type)
	t = template.loader.get_template(template_location)
        context[opt.object_name.lower()] = c_type
        return t.render(context)

def do_full_content(parser, token):
    """{% full_content content summary %}"""
    try:
        tag_name, content, template_type = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly two arguments" % token.contents.split()[0]
    return FullContentNode(content, template_type)

register.tag('full_content', do_full_content)
