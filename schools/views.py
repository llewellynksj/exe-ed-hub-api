from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import School, Review
from .serializers import SchoolSerializer, ReviewSerializer
from .filters import SchoolFilter, ReviewFilter


class SchoolViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  queryset = School.objects.all()
  serializer_class = SchoolSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_class = SchoolFilter
  search_fields = ['school_name', 'locality_name']
  ordering_fields = ['locality_name', 'school_name', 'school_level', 'ofsted']


class ReviewViewSet(ModelViewSet):
  """
  Single ViewSet that combines all operations for list and detail views
  """
  serializer_class = ReviewSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = ReviewFilter
  search_fields = ['username', 'school', 'title']

  def get_queryset(self):
    """
    Overide the get queryset method
    Returns the review objects filtered by the School id
    """
    return Review.objects.filter(school_id=self.kwargs['school_pk'])


  def get_serializer_context(self):
    """
    Provide the context for the serializer
    Returns the School id
    """
    return {'school_id': self.kwargs['school_pk']}