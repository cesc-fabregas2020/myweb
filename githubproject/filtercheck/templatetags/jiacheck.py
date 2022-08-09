from django import template

register = template.Library()

@register.filter
def addcha_jia(value,arg):
    return str(value)+str(arg)
 