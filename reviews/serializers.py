from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.Serializer):
  """
  Serializer to return JSON object of Review Model
  """
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