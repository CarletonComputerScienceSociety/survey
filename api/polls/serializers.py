from django.db.models import fields
from polls.models import (
    Poll,
    MultipleChoiceAnswer,
    MultipleChoiceQuestion,
    WrittenQuestion,
    Question,
    WrittenResponse,
    MultipleChoiceResponse,
    Submission,
)
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceAnswer
        fields = ["id", "answer_body"]


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    answers = MultipleChoiceAnswerSerializer(
        many=True, required=False, source="answers_list"
    )

    class Meta:
        model = MultipleChoiceQuestion
        fields = ["body", "answers", "id"]


class WrittenQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenQuestion
        fields = ["body"]


class QuestionSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MultipleChoiceQuestion: MultipleChoiceQuestionSerializer,
        WrittenQuestion: WrittenQuestionSerializer,
    }


class PollSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, required=False, source="questions_list")

    class Meta:
        model = Poll
        fields = ["id", "title", "description", "questions"]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id", "poll"]


class MultipleChoiceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceResponse
        fields = ["submission", "question_multiplechoice", "answer"]


class WrittenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenResponse
        fields = ["submission", "question_written", "answer_body"]


class ResponseSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MultipleChoiceResponse: MultipleChoiceResponseSerializer,
        WrittenResponse: WrittenResponseSerializer,
    }
