from django.urls import path
from rest_framework.routers import DefaultRouter
from schools import views

# Router code from 'Routers' chapter of 'The ultimate Django Part 2' course
# by Code with Mosh: https://codewithmosh.com/p/the-ultimate-django-part2
router = DefaultRouter()
router.register('schools', views.SchoolViewSet)
router.urls

urlpatterns = router.urls