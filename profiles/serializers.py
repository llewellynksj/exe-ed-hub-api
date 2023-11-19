from rest_framework import serializers
from .models import ParentProfile


class ParentProfileSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of Parent Profile model
  """
  username = serializers.ReadOnlyField(source='username.username')
  is_user = serializers.SerializerMethodField(method_name='get_is_user')

  def get_is_user(self, obj):
    request = self.context['request']
    return request.user == obj.username

  class Meta:
    model = ParentProfile
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'image',
      'first_name',
      'last_name',
      'is_user',
    ]
