from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from schools.models import School


class Review(models.Model):
  """
  School Review Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
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
