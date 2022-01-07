from django.db.models.query import QuerySet
from rest_framework import status, generics
from rest_framework.response import Response as R
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
            return R(final_data, 200)
        except Poll.DoesNotExist:
            final_data = {"data": {}, "errors": "Event not found"}
            return R(final_data, 404)
