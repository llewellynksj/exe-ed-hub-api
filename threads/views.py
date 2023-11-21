from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .filters import PostFilter, CommentFilter
from exe_ed_hub_api.permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
  """
  
  """
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_class = PostFilter
  search_fields = ['username', 'created_on', 'title', 'category',]
  ordering_fields = ['created_on', 'category',]

  def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]

class CommentViewSet(ModelViewSet):
  """
  
  """
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter,]
  filterset_class = CommentFilter
  search_fields = ['username', 'created_on',]


  def get_permissions(self):
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]


class LikeViewSet(ModelViewSet):
  """
  
  """
  queryset = Like.objects.all()
  serializer_class = LikeSerializer

def get_permissions(self):
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]
