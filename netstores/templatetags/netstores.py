from django import template

register = template.Library()


@register.inclusion_tag('tags/messages.html', takes_context=True)
def show_messages(context, show=True):
    return {'messages': (context.get('messages') if show else None)}


@register.inclusion_tag('tags/form_field_errors.html')
def show_form_field_errors(field_errors):
    return {'errors': field_errors}


@register.filter
def sales_list(value):
    return value.sellers.all().order_by('first_name')