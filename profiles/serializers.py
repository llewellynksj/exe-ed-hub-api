from django.db import IntegrityError
from rest_framework import serializers
from .models import ParentProfile, Follower


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


class FollowerSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of Follower model
  """
  username = serializers.ReadOnlyField(source='username.username')
  followed_name = serializers.ReadOnlyField(source='followed.username')

  class Meta:
      model = Follower
      fields = [
          'id',
          'username',
          'followed',
          'followed_name',
          'created_on',
      ]

  # Code from CI DRF-API walkthrough:
  def create(self, validated_data):
      try:
          return super().create(validated_data)
      except IntegrityError:
          raise serializers.ValidationError({
              'detail': 'duplicated follower'
          })