from django.urls import include, path
from .views import UserViewSet, GroupViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = router.urls
