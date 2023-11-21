from rest_framework import serializers
from .models import Item, Response


class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = [
      'id',
      'created_on',
      'updated_on',
      'username',
      'want_or_offer',
      'category',
      'title',
      'description',
      'location',
      'image',
      'is_live',
    ]