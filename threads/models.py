from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
  """
  Post Model
  Database for user post
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=255)
  content = models.TextField()
  category = models.CharField(max_length=255)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"{self.title} by {self.username}"


class Comment(models.Model):
  """
  Comment Model
  """
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.TextField()

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"Comment by {self.username}"
  


class Like(models.Model):
  """
  Like Model
  Stores relationship data between users and posts/comments they have liked
  """
  created_on = models.DateTimeField(auto_now_add=True)
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    unique_together = (('username', 'post',), ('username', 'comment',))
  
  def __str__(self):
    return f"{self.username}"
