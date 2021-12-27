from django.db.models import fields
from polls.models import Submission,MultipleChoiceResponse,WrittenResponse,WrittenQuestion,MultipleChoiceQuestion
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["id","poll"]


class MultipleChoiceResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceResponse
        fields = ["submission","question_multiplechoice","answer"]



class WrittenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenResponse
        fields = ["submission","question_written","answer_body"]


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ["poll","body",]


class WrittenQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenQuestion
        fields = ["poll","body",]

class ResponseSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MultipleChoiceResponse: MultipleChoiceResponseSerializer,
        WrittenResponse: WrittenResponseSerializer,
    }
