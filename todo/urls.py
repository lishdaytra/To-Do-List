from rest_framework import routers
from todo import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet, 'todo')
router.register(r'category', views.CategoryViewSet, basename='category')

urlpatterns = router.urls