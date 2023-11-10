from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from todo.serializers import CategorySerializer, TaskSerializer
from todo.models import Category, Task

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ('title','category', 'completed')
    search_fields = ('title',)
    ordering_fields = ('category','is_complete', 'created_at', 'created_end')
# Create your views here.
