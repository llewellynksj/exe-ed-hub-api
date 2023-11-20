from django.db import IntegrityError
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Post, Comment, Like

# Adapted from CI DRF-API walkthrough:

class PostSerializer(serializers.ModelSerializer):
  """
  
  """
  username = serializers.ReadOnlyField(source='username.username')
  is_user = serializers.SerializerMethodField(method_name='get_is_user')
  profile_id = serializers.ReadOnlyField(source='username.profile.id')
  profile_image = serializers.ReadOnlyField(source='username.profile.image.url')
  like_id = serializers.SerializerMethodField(method_name='get_like_id')
  likes_count = serializers.ReadOnlyField()
  comments_count = serializers.ReadOnlyField()

  def get_is_user(self, obj):
    request = self.context['request']
    return request.user == obj.username
  
  def get_like_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
        like = Like.objects.filter(
            username=user, post=obj).first()
        return like.id if like else None
    return None

  class Meta:
    model = Post
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'is_user',
      'profile_id',
      'profile_image',
      'title',
      'content',
      'category',
      'comments_count',
      'like_id',
      'like_count',
    ]


class CommentSerializer(serializers.ModelSerializer):
  """
  
  """
  username = serializers.ReadOnlyField(source='username.username')
  is_user = serializers.SerializerMethodField(method_name='get_is_user')
  profile_id = serializers.ReadOnlyField(source='username.profile.id')
  profile_image = serializers.ReadOnlyField(source='username.profile.image.url')
  like_id = serializers.SerializerMethodField(method_name='get_like_id')
  likes_count = serializers.ReadOnlyField()
  created_on = serializers.SerializerMethodField(method_name='get_created_on')
  updated_on = serializers.SerializerMethodField(method_name='get_updated_on')

  def get_is_user(self, obj):
    request = self.context['request']
    return request.user == obj.username

  def get_created_on(self, obj):
    return naturaltime(obj.created_at)

  def get_updated_on(self, obj):
    return naturaltime(obj.updated_at)
  
  def get_like_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
        like = Like.objects.filter(
            username=user, comment=obj).first()
        return like.id if like else None
    return None

  class Meta:
    model = Comment
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'is_user',
      'profile_id',
      'profile_image',
      'post',
      'comment',
      'like_id',
      'like_count',
    ]


class LikeSerializer(serializers.ModelSerializer):
  """
  
  """
  username = serializers.ReadOnlyField(source='username.username')

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