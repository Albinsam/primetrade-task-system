from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'owner', 'owner_name']