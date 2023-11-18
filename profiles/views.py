from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import ParentProfile
from .serializers import ParentProfileSerializer


class ParentProfileList(ListCreateAPIView):
  queryset = ParentProfile.objects.all()
  serializer_class = ParentProfileSerializer
  
  def get_serializer_context(self):
    return {'request': self.request}


class ParentProfileDetail(RetrieveUpdateDestroyAPIView):
  queryset = ParentProfile.objects.all()
  serializer_class = ParentProfileSerializer
