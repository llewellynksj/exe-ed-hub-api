from django.db import models
from django.contrib.auth.models import User
from .choices import WANTOROFFER, CATEGORY


class Item(models.Model):
  """
  Item Model
  Stores data on items available for exchange/recycle
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  want_or_offer = models.CharField(max_length=50, choices=WANTOROFFER)
  category = models.CharField(max_length=255, choices=CATEGORY)
  title = models.CharField(max_length=150)
  description = models.TextField()
  location = models.CharField(max_length=255)
  image = models.ImageField(
    upload_to='images/',
    default='../ExeEdHub/beep_boop_beep_robot_rohkhr'
  )
  is_live = models.BooleanField(default=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    f"{self.want_or_offer}: {self.title} - posted by {self.username}"


class Response(models.Model):
  """
  Response Model
  Records responses to the Item Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  comment = models.TextField()

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    f"Response by {self.username} to {self.item}"

