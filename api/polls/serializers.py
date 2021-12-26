from django.db.models import fields
from polls.models import (
    Poll,
    MultipleChoiceAnswer,
    MultipleChoiceQuestion,
    WrittenQuestion,
    Question,
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
        fields = ["id", "title", "description", "questions"]
