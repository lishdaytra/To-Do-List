from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_end = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE,
        default=0
    )

