from tasks.models import Task
from django.shortcuts import get_object_or_404

def get_all_tasks():
    return Task.objects.all()

def get_task_by_id(pk):
    return get_object_or_404(Task, pk=pk)

def create_task(data):
    return Task.objects.create(**data)

def update_task(task, data):
    for attr, value in data.items():
        setattr(task, attr, value)
    task.save()
    return task

def delete_task(task):
    task.delete()
