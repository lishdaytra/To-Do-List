from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet, 'todo')
urlpatterns = router.urls