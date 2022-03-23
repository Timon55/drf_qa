from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(verbose_name='Текст', max_length=250)
    num_right = models.IntegerField(verbose_name='Кол-во правильных ответов')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id']


    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text=models.CharField(verbose_name='Ответ', max_length=250)
    right = models.BooleanField(verbose_name='Правильный', default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['id']

    def __str__(self):
        return self.text

class Test(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=250)
    Questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['id']

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    theory = models.CharField(verbose_name='Теория', max_length=1000)
    tests = models.ManyToManyField(Test)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['id']

    def __str__(self):
        return self.title

class Test_Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.CharField(verbose_name='Результат', max_length=300)

    def __str__(self):
        return self.user.username

