from django.urls import path
from rest_framework.routers import DefaultRouter
from profiles import views

router = DefaultRouter()
router.register('profiles', views.ParentProfileViewSet)
router.urls

urlpatterns = router.urls
