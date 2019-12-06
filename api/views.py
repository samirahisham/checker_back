from django.shortcuts import render
from rest_framework.generics import (CreateAPIView,DestroyAPIView,ListAPIView,RetrieveUpdateAPIView)
from .serializers import ToDoSerializer,ItemSerializer,StatusSerializer
from checker.models import  ToDo,Item
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class CreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer

class ListView(ListAPIView):
    serializer_class =ItemSerializer
    queryset = Item.objects.all()

class DeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class DeleteAll(APIView):
    def delete(self, request, format=None):
        Item.objects.all().delete()
        return Response({})

class Status(RetrieveUpdateAPIView):
    serializer_class =StatusSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'