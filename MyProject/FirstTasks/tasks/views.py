from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers.task_serializer import TaskSerializer  # Adjust import if needed

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()  # Query the DB
    serializer = TaskSerializer(tasks, many=True)  # Serialize the data
    return Response(serializer.data, status=status.HTTP_200_OK)  # Return JSON
