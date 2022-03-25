from rest_framework import viewsets
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from edu_service.serializers import UserSerializer, GroupSerializer
from edu_service.permissions import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]