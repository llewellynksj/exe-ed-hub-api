from django.db import models


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
  city = models.CharField(max_length=100)
  postcode = models.CharField(max_length=10)
  ofsted = models.CharField(choices=OFSTED_RATING, max_length=50)

  class Meta:
    ordering = ['-school_name']
  
  def __str__(self):
    return f"{self.school_name} - {self.school_level}"

