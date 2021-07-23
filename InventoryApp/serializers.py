from django.db.models.base import Model
from rest_framework import serializers
from .models import *

class ServerDetails(serializers.ModelSerializer):
    class Meta:
        model = ServerInventory
        fields = "__all__"