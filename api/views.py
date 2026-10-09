from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Create, list, update, and delete tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
