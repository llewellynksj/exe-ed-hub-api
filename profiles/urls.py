from django.urls import path
from rest_framework_nested import routers
from profiles import views

# Router code from 'Routers' chapter of 'The ultimate Django Part 2' course
# by Code with Mosh: https://codewithmosh.com/p/the-ultimate-django-part2
router = routers.DefaultRouter()
router.register('profiles', views.ParentProfileViewSet)

profiles_router = routers.NestedDefaultRouter(router, 'profiles', lookup='profile')
profiles_router.register('followers', views.FollowerViewSet, basename='profile-followers')
profiles_router.register('dependents', views.DependentViewSet, basename='profile-dependents')

urlpatterns = router.urls + profiles_router.urls
