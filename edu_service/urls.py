from django.urls import include, path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = router.urls
