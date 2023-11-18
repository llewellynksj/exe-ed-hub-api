from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ParentProfileList.as_view()),
    # path('profiles/<int:pk>/', views.ParentProfileDetail.as_view()),
]