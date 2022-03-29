from django.contrib.auth.models import User, Group
from edu_service.models import *
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView


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


class TestResultSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Test_Result
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)

        test = Test.objects.get(id=data['testId'])
        user = User.objects.get(username=data['username'])

        test_result = Test_Result()
        test_result.test = test
        test_result.user = user

        questions = [q for q in test.questions.all()]
        answers = [data['answers'][a] for a in range(len(data['answers']))]

        answered_correct_count = 0
        for i in range(len(questions)):
            answers_for_question = questions[i].answers.all()
            num_right = questions[i].num_right
            right_answer = []
            if num_right == len([answers[i]]):
                for j in answers_for_question:
                    if j.right:
                        right_answer.append(j)
                if right_answer.sort() == [answers[i]].sort():
                    answered_correct_count += 1

        result = answered_correct_count / len(questions) * 100
        test_result.result = str(result)
        test_result.save()
        return test_result
