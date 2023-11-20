from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import ParentProfile, Follower, Dependent
from .serializers import ParentProfileSerializer, FollowerSerializer, DependentSerializer
from exe_ed_hub_api.permissions import IsOwnerOrReadOnly


class ParentProfileViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  queryset = ParentProfile.objects.all()
  serializer_class = ParentProfileSerializer
  
  def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]

  # def get_serializer_context(self):
  #   return {'request': self.request}


class FollowerViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  queryset = Follower.objects.all()
  serializer_class = FollowerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DependentViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  serializer_class = DependentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get_queryset(self):
    """
    Overide the get queryset method
    Returns the dependent objects filtered by the parent id
    """
    return Dependent.objects.filter(parent_id=self.kwargs['profile_pk'])

  def get_serializer_context(self):
    """
    Provide the context for the serializer
    Returns the parent id
    """
    return {'parent_id': self.kwargs['profile_pk']}