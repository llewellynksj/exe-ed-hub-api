from django_filters.rest_framework import FilterSet
from .models import School

class SchoolFilter(FilterSet):
  class Meta:
    model = School
    fields = {
      'school_name': ['icontains'],
      'locality_name': ['exact'],
      'school_level': ['exact'],
    }