from rest_framework import serializers
from todo.models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class TaskSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True,)
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'category',
            'description',
            'created_at',
            'completed',
            'date_end',
        )