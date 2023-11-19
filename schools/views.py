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
  serializer_class = ReviewSerializer

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