from rest_framework.routers import DefaultRouter
from apps.users.api.viewsets import UserViewset

router = DefaultRouter()
router.register(r'users', UserViewset, basename='users')

urlpatterns = router.urls