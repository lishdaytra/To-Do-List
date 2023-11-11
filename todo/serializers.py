from rest_framework import serializers
from todo.models import Task, Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'category',
            'description',
            'created_at',
            'completed',
            'created_end',
        )