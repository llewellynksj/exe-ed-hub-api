from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ParentProfile
from .serializers import ParentProfileSerializer


class ParentProfileList(APIView):
  def get (self, request):
    profiles = ParentProfile.objects.all()
    serializer = ParentProfileSerializer(profiles, many=True)
    return Response(serializer.data)
