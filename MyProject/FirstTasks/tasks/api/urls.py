from django.urls import path
from .views import GetTasks, CreateTask, TaskDetail

urlpatterns = [
    path('tasks/', GetTasks.as_view(), name='get_tasks'),
    path('tasks/create/', CreateTask.as_view(), name='create_task'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]
