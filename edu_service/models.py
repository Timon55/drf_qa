from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(verbose_name='Текст', max_length=250)
    num_right = models.IntegerField(verbose_name='Кол-во правильных ответов')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text=models.CharField(verbose_name='Ответ', max_length=250)
    right = models.BooleanField(verbose_name='Правильный', default=False)

class Test(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=250)
    Questions = models.ManyToManyField(Question)

class Topic(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    theory = models.CharField(verbose_name='Теория', max_length=1000)
    tests = models.ManyToManyField(Test)

class Test_Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.CharField(verbose_name='Результат', max_length=300)

