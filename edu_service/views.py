from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from edu_service.models import *
from rest_framework.permissions import IsAuthenticated
from edu_service.serializers import *
from edu_service.permissions import *
from rest_framework.generics import ListAPIView, CreateAPIView


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


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer
    permission_classes = [IsAuthenticated]


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TheoryListSerializer
    permission_classes = [IsAuthenticated]


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]



class TestResultsListView(ListAPIView):
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Test_Result.objects.all()
        #print(self.request.query_params)
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class TestResultsCreateView(CreateAPIView):
    serializer_class = TestResultSerializer
    queryset = Test_Result.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.user)
        print(request.data)
        serializer = TestResultSerializer(data=request.data)
        serializer.is_valid()
        test_result = serializer.create(request)
        if test_result:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)





