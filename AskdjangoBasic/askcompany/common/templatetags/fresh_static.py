from time import time
from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

register = template.Library()

class FreshStaticNode(StaticNode):
    def url(self, context):
        url = super().url(context)
        if settings.DEBUG: #개발 모드일 때
            url += '?_={}'.format(int(time())) # 더미 추가
        return url

@register.tag('fresh_static') 
def do_static(parser, token):
    return FreshStaticNode.handle_token(parser, token)