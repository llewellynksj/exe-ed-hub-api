from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class ParentProfile(models.Model):
  """
  Parent Profile Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  image = model.ImageField(
    upload_to='images/',
    default='../ExeEdHub/sleep_glasses_vmomqy'
  )
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return f"{self.username} created on {self.created_on}"
  

# Function using signals to create profile automatically
# from CI DRF-API walkthrough:
def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile automatically when a User is created
    """
    if created:
        Profile.objects.create(username=instance)


post_save.connect(create_profile, sender=User)
  
