from django.db import models
from django.contrib.auth.models import User
from .choices import SCHOOL_LEVEL, OFSTED_RATING, LOCALITY_NAME, RATINGS

class School(models.Model):
  """
  School Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  school_name = models.CharField(max_length=255)
  school_level = models.CharField(choices=SCHOOL_LEVEL, max_length=255)
  street_address = models.CharField(max_length=255)
  locality_name = models.CharField(max_length=255, choices=LOCALITY_NAME)
  postcode = models.CharField(max_length=10)
  ofsted = models.CharField(choices=OFSTED_RATING, max_length=50)
  overall_rating = models.CharField(default="This school does not yet have any reviews", max_length=255)

  class Meta:
    ordering = ['-school_name']
  
  def __str__(self):
    return f"{self.school_name} - {self.school_level}"


class Review(models.Model):
  """
  School Review Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.CharField(max_length=100)
  school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='reviews')
  title = models.CharField(max_length=255)
  review = models.TextField()
  teaching_quality = models.PositiveSmallIntegerField(choices=RATINGS)
  admin_service = models.PositiveSmallIntegerField(choices=RATINGS)
  child_happiness = models.PositiveSmallIntegerField(choices=RATINGS)
  atmosphere = models.PositiveSmallIntegerField(choices=RATINGS)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"{self.school}: {self.title} by {self.username}"
