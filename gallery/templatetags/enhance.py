from django import template

register=template.Library()

@register.filter(name='enhance')
def enhance(name,b):
    return f'{name} Kaise ho! {b}'