from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import ParentProfile
from .serializers import ParentProfileSerializer


class ParentProfileViewSet(ModelViewSet):
  queryset = ParentProfile.objects.all()
  serializer_class = ParentProfileSerializer

  # def get_serializer_context(self):
  #   return {'request': self.request}
