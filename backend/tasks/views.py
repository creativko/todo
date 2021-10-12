from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response


from .serializers import TaskListSerializers, TaskDetailSerializers
from .models import Task


class TasksList(generics.ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskListSerializers


class TaskCreate(generics.CreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializers


class TaskDelete(generics.DestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializers


class TaskUpdate(generics.UpdateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializers
