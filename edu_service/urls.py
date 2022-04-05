from django.urls import include, path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'topics/<int:pk>', TopicViewSet)
router.register(r'theory', TheoryViewSet)
router.register(r'theory/<int:pk>', TheoryViewSet)
router.register(r'test', TestViewSet)
router.register(r'test/<int:pk>', TestViewSet)

urlpatterns = router.urls

urlpatterns += [path('test-result/', TestResultsListView.as_view()),
                path('test-result/create/', TestResultsCreateView.as_view()),
                path('user-answer/', UserAnswerListView.as_view()),
                path('user-answer/create/', UserAnswerCreateView.as_view())
                ]
