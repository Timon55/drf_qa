from django.contrib.auth.models import User, Group
from edu_service.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['text','answers']


class TopicListSerializer(serializers.ModelSerializer):
    tests = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    Questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['title', 'Questions']


