from rest_framework.viewsets import ModelViewSet
from .models import School, Review
from .serializers import SchoolSerializer, ReviewSerializer


class SchoolViewSet(ModelViewSet):
  """
  
  """
  queryset = School.objects.all()
  serializer_class = SchoolSerializer


class ReviewViewSet(ModelViewSet):
  """
  one view set that combines all operations for viewing list and detail
  """
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer