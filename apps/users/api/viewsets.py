from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


    # def list(self, request):
    #     users = self.get_queryset()
    #     user_serializer = self.list_serializer_class(users, many=True)
    #     return Response(user_serializer.data, status=status.HTTP_200_OK)