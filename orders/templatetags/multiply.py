from django import template

register = template.Library()

# We are using decerator to register our template function
# we have to use generative function, contains yeild instead of return
@register.simple_tag(name='multiply')
def multiply(a,b):
    return a*b