from django import template
import re
from boto.s3 import Connection

register = template.Library()

class GetBuckets(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = Connection().get_all_buckets()
        return ''

@register.tag
def get_buckets(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, \
                     '%s tag requires arguments.' %  token.contents.split()[0]
    match = re.search(r'[.]*as (\w+)', arg)
    if not match:
        raise template.TemplateSyntaxError, \
               '%s tag requires an argument of a context variable.' % tag_name
    var_name = match.groups()[0]
    return GetBuckets(var_name)
    
@register.tag
def list_bucket(parser, token):
    pass


@register.tag
def get_object_info(parser, token):
    pass