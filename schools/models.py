from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class School(models.Model):
  """
  School Model
  """
  SCHOOL_LEVEL = [
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Sixth Form/College', 'Sixth Form/College'),
  ]

  OFSTED_RATING = [
    ('Outstanding', 'Outstanding'),
    ('Good', 'Good'),
    ('Requires Improvement', 'Requires Improvement'),
    ('Inadequate', 'Inadequate'),
  ]

  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  school_name = models.CharField(max_length=255)
  school_level = models.CharField(choices=SCHOOL_LEVEL, max_length=255)
  street_address = models.CharField(max_length=255)
  locality_name = models.CharField(max_length=100)
  postcode = models.CharField(max_length=10)
  ofsted = models.CharField(choices=OFSTED_RATING, max_length=50)

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
  teaching_quality = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  admin_service = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  child_happiness = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  atmosphere = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"{self.school}: {self.title} by {self.username}"
