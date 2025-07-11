from django import template

register = template.Library()

@register.filter
def filter_category(files, category_type):
    return [f for f in files if f.category == category_type]