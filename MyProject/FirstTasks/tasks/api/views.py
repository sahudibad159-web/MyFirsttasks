from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Task
from tasks.serializers.task_serializer import TaskSerializer
from tasks.services import tasks_service  

class GetTasks(APIView):
    def get(self, request):
        tasks = tasks_service.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class CreateTask(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get(self, request, pk):
        task = tasks_service.get_task_by_id(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = tasks_service.get_task_by_id(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = tasks_service.get_task_by_id(pk)
        tasks_service.delete_task(task)
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
