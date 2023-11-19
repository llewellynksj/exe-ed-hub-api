from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(ModelViewSet):
  """
  one view set that combines all operations for viewing list and detail
  """
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer