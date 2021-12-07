from django.shortcuts import render
from polls.serializers import SubmissionSerializer,MultipleChoiceResponseSerializer,WrittenResponseSerializer, MultipleChoiceQuestionSerializer, WrittenQuestionSerializer
from django.db.models.query import QuerySet

from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Submission,Poll,MultipleChoiceResponse,MultipleChoiceQuestion,MultipleChoiceAnswer\
,MultipleChoiceAnswer,WrittenResponse,WrittenQuestion, MultipleChoiceQuestion



# Create your views here.


class SubmissionList(generics.GenericAPIView):  
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
      
    def post(self, request):  
        #serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        print(request.data)
        #prints the swagger box its a dict
        #takes poll from the swagger box and passes it into the submission model
        poll = Poll.objects.get(id=request.data['poll'])
        submission = Submission.objects.create(poll=poll)
        print(submission)
        
        #print(serializer)
        serializer = self.serializer_class(submission)
        return Response(serializer.data,status=201)
    

class MultipleChoiceResponseList(generics.GenericAPIView):
    queryset = MultipleChoiceResponse.objects.all()
    serializer_class = MultipleChoiceResponseSerializer

    def post(self, request):  
        submission = Submission.objects.get(id=request.data['submission'])
        print(request.data)
        #get the question object from the given id
        question_multiplechoice= MultipleChoiceQuestion.objects.get(id=request.data['question_multiplechoice'])
        
        #get the answer content
        #will get answer object
        answer= request.data['answer']
        #create answer object in the MultipleChoiceAnswer
        multiple_answer_create= MultipleChoiceAnswer.objects.create(answer_body=answer,multiple_choice_question=question_multiplechoice)
        print('hi',request.data,multiple_answer_create)

        #create response object given all the data

        mrc = MultipleChoiceResponse.objects.create(submission=submission,question_multiplechoice=question_multiplechoice,answer=multiple_answer_create)
        print(mrc)
        
        #print(serializer)
        serializer = self.serializer_class(mrc)
        return Response(serializer.data,status=201)
        
        #question can be seperate but answer will come with the response 
        #is onus of checking for multiple/written on backend or frontend
        #2 approaches make both in this and check for type or front end will call the correct one depending on the question
        #for now its seperate
        #why does swagger show string

class WrittenResponseList(generics.GenericAPIView):
    queryset = WrittenResponse.objects.all()
    serializer_class = WrittenResponseSerializer

    def post(self, request):  
        submission = Submission.objects.get(id=request.data['submission'])
        print(request.data)
        question_written= WrittenQuestion.objects.get(id=request.data['question_written'])
        answer= request.data['answer_body']
        #dont need this because of how written is structured
        #written_answer_create= MultipleChoiceAnswer.objects.create(answer_body=answer,multiple_choice_question=question_multiplechoice)
        print('hi',request.data)
        writtenresponse = WrittenResponse.objects.create(submission=submission,question_written=question_written,answer_body=answer)
        print(writtenresponse)
        
        #print(serializer)
        serializer = self.serializer_class(writtenresponse)
        return Response(serializer.data,status=201)

#discrepancy between mode of multiple and written

class MultipleChoiceQuestionList(generics.GenericAPIView):
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer

    def post(self, request):  
        poll = Poll.objects.get(id=request.data['poll'])
        body= request.data['body']
        #print('hi',request.data)
        mult_ques = MultipleChoiceQuestion.objects.create(poll=poll,body=body)
        #print(mult_ques)
        
        serializer = self.serializer_class(mult_ques)
        return Response(serializer.data,status=201)


class WrittenQuestionList(generics.GenericAPIView):
    queryset = WrittenQuestion.objects.all()
    serializer_class = WrittenQuestionSerializer

    def post(self, request):  
        poll = Poll.objects.get(id=request.data['poll'])
        print(request.data)
        body= request.data['body']
        
        #print('hi',request.data)
        mult_ques = WrittenQuestion.objects.create(poll=poll,body=body)
        #print(mult_ques)
        

        serializer = self.serializer_class(mult_ques)
        return Response(serializer.data,status=201)