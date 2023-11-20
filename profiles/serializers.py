from django.db import IntegrityError
from rest_framework import serializers
from .models import ParentProfile, Follower, Dependent


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


class DependentSerializer(serializers.ModelSerializer):
  """
  Serializer to return JSON object of Dependent model
  """
  school_name = serializers.ReadOnlyField(source='school.school_name')

  class Meta:
    model = Dependent
    fields = [
      'id',
      'created_on',
      'updated_on',
      'name',
      'age',
      'school',
      'school_name',
    ]
  
  def create(self, validated_data):
    """
    Overides create method for creating a Dependent
    Reads the parent id from context
    Returns Dependent object
    """
    parent_id = self.context['parent_id']
    return Dependent.objects.create(parent_id=parent_id, **validated_data)
