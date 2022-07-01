from rest_framework.routers import DefaultRouter 
from .viewsets import CategoryViewset

router = DefaultRouter()

router.register(r'categories', CategoryViewset, basename='categories')

urlpatterns = router.urls