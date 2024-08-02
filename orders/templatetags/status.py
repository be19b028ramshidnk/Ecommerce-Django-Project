from django import template

register = template.Library()

# We are using decerator to register our template function
# we have to use generative function, contains yeild instead of return
@register.simple_tag(name='status')
def status(a):
    if a == 1:
        return "ORDER_CONFIRMED"
    elif a==2:
        return "ORDER_PROCESSED"
    elif a==3:
        return "ORDER_DELIVERED"
    else:
        return "ORDER_REJECTED"