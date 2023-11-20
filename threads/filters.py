from django_filters.rest_framework import FilterSet
from .models import Post, Comment

class PostFilter(FilterSet):
  class Meta:
    model = Post
    fields = {
      'username': ['exact'],
      'category': ['exact'],
      'title': ['icontains'],
    }


class CommentFilter(FilterSet):
  class Meta:
    model = Comment
    fields = {
      'username': ['exact'],
      'comment': ['icontains'],
    }