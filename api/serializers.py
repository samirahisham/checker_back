
from django.contrib.auth.models import User
from rest_framework import serializers
from checker.models import (ToDo,Item)

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields='__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=['status']
