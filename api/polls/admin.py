from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionResource(admin.ModelAdmin):
    list_display = ["id", "body", "poll"]


@admin.register(Poll)
class PollResource(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionResource(admin.ModelAdmin):
    list_display = ["id", "body", "poll"]


@admin.register(MultipleChoiceAnswer)
class MultipleChoiceAnswerResource(admin.ModelAdmin):
    list_display = ["id", "answer_body", "multiple_choice_question"]


@admin.register(WrittenQuestion)
class WrittenQuestionResource(admin.ModelAdmin):
    list_display = ["id", "body", "poll"]


@admin.register(Submissions)
class SubmissionResource(admin.ModelAdmin):
    list_display = ["id", "poll"]


@admin.register(Responses)
class ResponseResource(admin.ModelAdmin):
    list_display = [
        "id",
        "submissions",
    ]


@admin.register(MultipleChoiceResponses)
class MultipleChoiceResponseResource(admin.ModelAdmin):
    list_display = ["id", "submissions", "question_multiplechoice", "answer"]


@admin.register(WrittenResponses)
class WrittenResponseResource(admin.ModelAdmin):
    list_display = ["id", "question_written", "answer_body"]
