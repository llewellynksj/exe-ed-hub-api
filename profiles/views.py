from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import ParentProfile, Follower
from .serializers import ParentProfileSerializer, FollowerSerializer


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
