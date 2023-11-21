from django.urls import path
from rest_framework_nested import routers
from exchanges import views

# Router code from 'Routers' chapter of 'The ultimate Django Part 2' course
# by Code with Mosh: https://codewithmosh.com/p/the-ultimate-django-part2
router = routers.DefaultRouter()
router.register('exchanges', views.ItemViewSet)

exchanges_router = routers.NestedDefaultRouter(router, 'exchanges', lookup='exchange')
exchanges_router.register('responses', views.ResponseViewSet, basename='exchange-responses')

urlpatterns = router.urls + exchanges_router.urls