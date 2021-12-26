from django.db.models.query import QuerySet
from rest_framework import status, generics
from rest_framework.response import Response
from .models import *
from django.db import models
from rest_framework import serializers
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
