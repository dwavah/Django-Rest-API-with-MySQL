from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user', 'name', 'model', 'cost']
        read_only_fields = ['user']
