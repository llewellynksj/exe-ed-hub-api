from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of School Model
  """
  school_name = serializers.ReadOnlyField(source='school.school_name')

  class Meta:
    model = School
    fields = [
      'id',
      'created_on',
      'updated_on',
      'school_name',
      'school_level',
      'street_address',
      'city',
      'postcode',
      'ofsted',
    ]