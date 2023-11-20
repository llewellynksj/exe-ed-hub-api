from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from exe_ed_hub_api.permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
  """"""
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]

class CommentViewSet(ModelViewSet):
  """"""
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]


class LikeViewSet(ModelViewSet):
  """"""
  queryset = Like.objects.all()
  serializer_class = LikeSerializer