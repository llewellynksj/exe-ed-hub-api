from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Item, Response
from .serializers import ItemSerializer, ResponseSerializer
from exe_ed_hub_api.permissions import IsOwnerOrReadOnly


class ItemViewSet(ModelViewSet):
  """
  
  """
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

  def get_permissions(self):
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]


class ResponseViewSet(ModelViewSet):
  """
  
  """
  queryset = Response.objects.all()
  serializer_class = ResponseSerializer

  def get_permissions(self):
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    else:
        permission_classes = [IsOwnerOrReadOnly]
    return [permission() for permission in permission_classes]
