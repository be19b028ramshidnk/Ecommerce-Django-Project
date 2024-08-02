from django import template

register = template.Library()

# We are using decerator to register our template function
# we have to use generative function, contains yeild instead of return
@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    count =0
    for data in list_data:
        chunk.append(data)
        count +=1
        if count == chunk_size:
            yield chunk
            count =0
            chunk = []
    if chunk:
        yield chunk