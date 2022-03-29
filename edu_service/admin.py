from django.contrib import admin
from edu_service.models import *

class AnswersInLine(admin.TabularInline):
    model = Answer
    extra = 4

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersInLine]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Topic)
admin.site.register(Answer)
admin.site.register(Test_Result)
