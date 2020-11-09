
from BlogApp.models import Post
from django import template
from django.utils.safestring import mark_safe
import markdown

register=template.Library()


@register.simple_tag(name='my_tag')
def total_post():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_posts55.html')
def show_latest_posts(count=2):
    latest_posts=Post.objects.order_by("-publish")[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count

@register.inclusion_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))