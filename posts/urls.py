from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('', PostViewSet, base_name='posts')
router.register('users', UserViewSet, base_name='users')

urlpatterns = router.urls
