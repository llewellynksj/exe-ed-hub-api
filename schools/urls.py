from django.urls import path
from rest_framework_nested import routers
from schools import views

# Router code from 'Nested Routers' chapter of 'The ultimate Django Part 2' course
# by Code with Mosh: https://codewithmosh.com/p/the-ultimate-django-part2
router = routers.DefaultRouter()
router.register('schools', views.SchoolViewSet)

schools_router = routers.NestedDefaultRouter(router, 'schools', lookup='school')
schools_router.register('reviews', views.ReviewViewSet, basename='school-reviews')

urlpatterns = router.urls + schools_router.urls