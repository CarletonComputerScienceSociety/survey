from django.db.models import fields
from polls.models import (
    Poll,
    MultipleChoiceAnswer,
    MultipleChoiceQuestion,
    WrittenQuestion,
    Question,
    MultipleChoiceResponse,
    WrittenResponse,
    Submission
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
        fields = ["body", "answers"]


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
        fields = ["id", "url", "title", "description", "questions"]





class MultipleChoiceResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleChoiceResponse
        fields = ["body", "answer"]


class WrittenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenResponse
        fields = ["answer_body"]

class ResponseSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MultipleChoiceResponse: MultipleChoiceResponseSerializer,
        WrittenResponse: WrittenResponseSerializer,
    }

class SubmissionSerializer(serializers.ModelSerializer):

    responses = ResponseSerializer(many=True, required=False, source="responses_list")

    class Meta:
        model = Submission
        fields = ["responses"]

class PollStatisticsSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, required=False, source="questions_list")
    class Meta:
        model = Poll
        fields = ["id", "url", "title", "description", "questions"]