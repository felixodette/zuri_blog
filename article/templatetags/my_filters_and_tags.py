from django import template
from django.utils import timezone
import math
import datetime

register = template.Library()

@register.filter(name='transfer')
def transfer(value, arg):
    return arg

@register.filter()
def lower(value):
    return value.lower()

@register.filter(name='timesince_zh')
def time_since_zh(value):
    now = timezone.now()
    diff = now - value

    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        return 'Just'

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        return str(math.floor(diff.seconds / 60)) + "minutes ago"

    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        return str(math.floor(diff.seconds / 3600)) + "An hour ago"

    if diff.days >= 1 and diff.days < 30:
        return str(diff.days) + "Days ago"

    if diff.days >= 30 and diff.days < 365:
        return str(math.floor(diff.days / 30)) + "Months ago"

    if diff.days >= 365:
        return str(math.floor(diff.days / 365)) + "Years ago"

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('article/tag_list.html')
def show_comments_pub_time(article):
    comments = article.comments.all()
    return {'comments': comments}