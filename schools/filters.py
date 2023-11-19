from django_filters.rest_framework import FilterSet
from .models import School, Review

class SchoolFilter(FilterSet):
  class Meta:
    model = School
    fields = {
      'school_name': ['icontains'],
      'locality_name': ['exact'],
      'school_level': ['exact'],
    }


class ReviewFilter(FilterSet):
  class Meta:
    model = Review
    fields = {
      'teaching_quality': ['exact'],
      'admin_service': ['exact'],
      'child_happiness': ['exact'],
      'atmosphere': ['exact'],
    }