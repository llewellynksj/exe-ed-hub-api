from django.db import IntegrityError
from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
  """
  
  """
  username = serializers.ReadOnlyField(source='username.username')

  class Meta:
    model = Post
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'title',
      'content',
      'category',
    ]


class CommentSerializer(serializers.ModelSerializer):
  """
  
  """
  username = serializers.ReadOnlyField(source='username.username')

  class Meta:
    model = Comment
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'post',
      'comment',
    ]


class LikeSerializer(serializers.ModelSerializer):
  """
  
  """
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
      model = Like
      fields = [
          'id',
          'created_on',
          'username',
          'post',
          'comment',
      ]

  # Function from CI DRF-API walkthrough:
  def create(self, validated_data):
      try:
          return super().create(validated_data)
      except IntegrityError:
          raise serializers.ValidationError({
              'detail': 'possible duplicate'
          })