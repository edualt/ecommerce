from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework.response import Response

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissions]


    def list(self, request):
        permission_classes = [DjangoModelPermissions.authenticated_users_only]
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        permission_classes = [DjangoModelPermissions.has_permission]
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User was created successfully'},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
             