from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostViewSet(ModelViewSet):
  """"""
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(ModelViewSet):
  """"""
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeViewSet(ModelViewSet):
  """"""
  queryset = Like.objects.all()
  serializer_class = LikeSerializer