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


class ReviewSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of Review Model
  """
  overall_rating = serializers.SerializerMethodField(method_name='calculate_overall_rating')

  def calculate_overall_rating(self, review: Review):
    """"""
    total_score = review.teaching_quality + review.admin_service + review.child_happiness + review.atmosphere
    return total_score / 20 * 100

  class Meta:
    model = Review
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'title',
      'review',
      'teaching_quality',
      'admin_service',
      'child_happiness',
      'atmosphere',
      'overall_rating',
    ]

  def create(self, validated_data):
    """
    Overides create method for creating a Review
    Reads the School id from context
    Returns Review object
    """
    school_id = self.context['school_id']
    return Review.objects.create(school_id=school_id, **validated_data)