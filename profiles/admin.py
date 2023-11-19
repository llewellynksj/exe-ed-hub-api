from django.contrib import admin
from .models import ParentProfile, Dependent, Follower

admin.site.register(ParentProfile)
admin.site.register(Dependent)
admin.site.register(Follower)
