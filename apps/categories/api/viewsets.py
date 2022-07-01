from gzip import READ
from rest_framework import viewsets, status
from apps.categories.api.serializers import CategorySerializer
from apps.categories.models import Category
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        permission_classes = [IsAdminUser]
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)