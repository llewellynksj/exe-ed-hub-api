from rest_framework import serializers
from .models import ParentProfile


class ParentProfileSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of Parent Profile model
  """
  username = serializers.ReadOnlyField(source='username.username')

  class Meta:
    model = ParentProfile
    fields = [
      'id', 'created_on', 'updated_on', 'username', 'image', 'first_name', 'last_name',
    ]
