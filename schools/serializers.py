from rest_framework import serializers
from .models import School, Review

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


class ReviewSerializer(serializers.Serializer):
  """
  Serializer to return JSON object of Review Model
  """
  username = serializers.ReadOnlyField(source='username.username')
  school = serializers.ReadOnlyField(source='school.school_name')

  class Meta:
    model = Review
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'school',
      'title',
      'review',
      'teaching_quality',
      'admin_service',
      'child_happiness',
      'atmosphere',
    ]