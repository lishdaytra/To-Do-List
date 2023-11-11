from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Task(models.Model):
    title = models.CharField(max_length=128, null=False)
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE,
        default=0
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    created_end = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, category: {self.category}'


