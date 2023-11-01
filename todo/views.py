from django.shortcuts import render
from rest_framework import viewsets
from todo.serializers import CategorySerializer, TaskSerializer
from todo.models import Category, Task

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# Create your views here.
