from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import ParentProfile, Follower, Dependent
from .serializers import ParentProfileSerializer, FollowerSerializer, DependentSerializer


class ParentProfileViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  queryset = ParentProfile.objects.all()
  serializer_class = ParentProfileSerializer

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