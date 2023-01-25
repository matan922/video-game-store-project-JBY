from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from rest_framework.response import Response
from rest_framework import status
from profile_user.serializers import ProfileSerializer
from .models import Profile
from rest_framework.views import APIView


# Create your views here.

# ------------------------- PROFILE START ------------------------- #
@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
class ProfileView(APIView):
    def get(self,request):
            user = request.user
            my_user = Profile.objects.get(user = user)
            serializer = ProfileSerializer(my_user)
            return Response(serializer.data, status = status.HTTP_200_OK)

    def patch(self,request):
            pk = request.data["pk"]
            profile = Profile.objects.get(pk = pk)
            serializer = ProfileSerializer(profile, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# ------------------------- PROFILE END ------------------------- #
