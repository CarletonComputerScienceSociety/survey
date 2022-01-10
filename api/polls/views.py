from django.db.models.query import QuerySet
from rest_framework import status, generics
from rest_framework.response import Response
from .models import (
    Submission,
    Poll,
    MultipleChoiceResponse,
    MultipleChoiceQuestion,
    MultipleChoiceAnswer,
    MultipleChoiceAnswer,
    WrittenResponse,
    WrittenQuestion,
    MultipleChoiceQuestion,
    Question,
)


from django.db import models
from rest_framework import serializers, status  
from uuid import UUID
from .serializers import *


# Details of selected Organization
class PollDetails(generics.RetrieveAPIView):

    serializer_class = PollSerializer

    def get(self, request, id):
        try:
            poll = Poll.objects.get(id=id)
            serializer = PollSerializer(poll, many=False)
            final_data = {"data": serializer.data, "errors": None}
            return Response(final_data, status=status.HTTP_200_OK)
        except Poll.DoesNotExist:
            final_data = {"data": {}, "errors": "Event not found"}
            return Response(final_data, status=status.HTTP_404_NOT_FOUND)


class SubmissionList(generics.GenericAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def post(self, request):
        poll = Poll.objects.get(id=request.data["poll"])
        submission = Submission.objects.create(poll=poll)
        serializer = self.serializer_class(submission)
        return Response(serializer.data, status=201)


class ResponseList(generics.GenericAPIView):
    queryset = MultipleChoiceResponse.objects.all()
    serializer_class = ResponseSerializer

    def post(self, request):
        # loops through each given dataset
        for i in request.data["data"]:
            question_type = Question.objects.get(
                id=i["question"]
            )  # get question object
            if isinstance(
                question_type, MultipleChoiceQuestion
            ):  # check if belongs to MultipleChoiceQuestion
                # get submission,question,answer objects
                submission = Submission.objects.get(id=i["submission"])
                question_multiplechoice = MultipleChoiceQuestion.objects.get(
                    id=i["question"]
                )
                answer = MultipleChoiceAnswer.objects.get(id=i["answer"])

                # create response object given all the data
                multiple_choice_response_create = MultipleChoiceResponse.objects.create(
                    submission=submission,
                    question_multiplechoice=question_multiplechoice,
                    answer=answer,
                )
                serializer = self.serializer_class(multiple_choice_response_create)
            elif isinstance(question_type, WrittenQuestion):
                submission = Submission.objects.get(id=i["submission"])
                question_written = WrittenQuestion.objects.get(id=i["question"])
                answer = i["answer"]
                writtenresponse_create = WrittenResponse.objects.create(
                    submission=submission,
                    question_written=question_written,
                    answer_body=answer,
                )
                serializer = self.serializer_class(writtenresponse_create)

        return Response(serializer.data, status=201)
