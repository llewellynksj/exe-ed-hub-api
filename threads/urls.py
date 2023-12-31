from django.urls import path
from rest_framework_nested import routers
from threads import views

# Router code from 'Nested Routers' chapter of 'The ultimate Django Part 2' course
# by Code with Mosh: https://codewithmosh.com/p/the-ultimate-django-part2
router = routers.DefaultRouter()
router.register('threads', views.PostViewSet)

posts_router = routers.NestedDefaultRouter(router, 'threads', lookup='post')
posts_router.register('comments', views.CommentViewSet, basename='threads-comments')

urlpatterns = router.urls + posts_router.urls