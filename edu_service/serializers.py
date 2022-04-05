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
        fields = ['id', 'text', 'answers']


class UserAnswersSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserAnswer
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)
        print(request.user)
        question = Question.objects.get(id=data['questionId'])
        user = User.objects.get(username=request.user)
        testId = Test.objects.get(id=data['testId'])
        answers = data['answers']
        user_answer = UserAnswer()
        user_answer.user = user
        user_answer.question = question
        user_answer.testId = testId
        user_answer.answers = answers
        answers_for_question = question.answers.all()
        right_answer = []
        list_answers = answers.split(',')
        for j in answers_for_question:
            if j.right:
                right_answer.append(j.text)
        print(right_answer)
        print(list_answers)
        print(right_answer == list_answers)
        if right_answer == list_answers:
            right = True
        else:
            right = False
        user_answer.right = right
        user_answer.save()
        return user_answer



class TopicListSerializer(serializers.ModelSerializer):
    tests = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = '__all__'

class TheoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ['id','theory']


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'title', 'questions']


class TestResultSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Test_Result
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)
        print(request.user)
        test = Test.objects.get(id=data['testId'])
        user = User.objects.get(username=request.user)

        test_result = Test_Result()
        test_result.test = test
        test_result.user = user
        answered_correct_count = 0
        answers = UserAnswer.objects.filter(user__username=request.user, testId=test)
        for a in answers:
            if a.right:
                answered_correct_count +=1
        result = answered_correct_count / len(answers) * 100
        full_result = 'Количество правильных ответов: ' + str(answered_correct_count) + '\n'
        full_result += 'Количество неправильных ответов: ' + str((len(answers)-answered_correct_count)) + '\n'
        full_result += 'Количество баллов: ' + str(result) + '\n'
        test_result.result = full_result
        print(test_result.result)
        test_result.save()
        return test_result
