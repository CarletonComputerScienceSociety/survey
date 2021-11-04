from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionResource(admin.ModelAdmin):
    list_display = ["id", "body"]


@admin.register(Poll)
class PollResource(admin.ModelAdmin):
    list_display = ["id", "description"]


@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionResource(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(MultipleChoiceAnswer)
class MultipleChoiceAnswerResource(admin.ModelAdmin):
    list_display = ["id", "answer_body", "multiple_choice_question"]


@admin.register(WrittenQuestion)
class WrittenQuestionResource(admin.ModelAdmin):
    list_display = ["id"]
