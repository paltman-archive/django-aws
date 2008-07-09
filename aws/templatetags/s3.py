from django.template import TemplateSyntaxError, Node, Library
from boto.s3 import Connection

register = Library()


class GetBuckets(Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = Connection().get_all_buckets()
        return ''

@register.tag
def get_buckets(parser, token):
    """{% get_buckets as [varname] %}"""
    args = token.contents.split()
    if len(args) != 3:
        raise TemplateSyntaxError, "get_buckets takes exactly 2 arguments."
    if args[1] != 'as':
        raise TemplateSyntaxError, "get_buckets first argument must be 'as'"
    return GetBuckets(args[2])
   
    

class ListBucket(Node):
    def __init__(self, bucket, var_name, prefix=None):
        self.bucket = bucket
        self.var_name = var_name
        self.prefix = ''
        if prefix:
            self.prefix = prefix
    def render(self, context):
        context[self.var_name] = Connection().get_bucket(self.bucket).list(self.prefix)
        return ''
    
@register.tag
def list_bucket(parser, token):
    """{% list_bucket [bucket_name] [prefix] as [varname] %}"""
    args = token.contents.split()
    if len(args) not in (4,5):
        raise TemplateSyntaxError, "list_bucket takes 4 or 5 arguments"
    if (len(args) == 4 and args[2] != 'as') or \
       (len(args) == 5 and args[3] != 'as'):
        raise TemplateSyntaxError, "list_bucket must set a variable with 'as'"
    if (len(args) == 4):
        return ListBucket(bucket=args[1].replace('"',''), var_name=args[3])
    if (len(args) == 5):
        return ListBucket(bucket=args[1].replace('"',''), prefix=args[2].replace('"',''), var_name=args[4])



class GetObjectInfo(Node):
    def __init__(self, bucket, key, var_name):
        self.bucket = bucket
        self.key = key
        self.var_name = var_name
    def render(self, context):
        key = Connection().get_bucket(self.bucket).get_key(self.key)
        print key, key.name, key.size
        context[self.var_name] = key
        return ''

@register.tag
def get_object_info(parser, token):
    """{% get_object_info [bucket_name] [key_name] as [varname] %}"""
    args = token.contents.split()
    if len(args) != 5:
        raise TemplateSyntaxError, "get_object_info takes exactly 5 arguments"
    if args[3] != 'as':
        raise TemplateSyntaxError, "get_object_info must set a variable"
    return GetObjectInfo(bucket=args[1].replace('"',''), key=args[2].replace('"',''), var_name=args[4])

