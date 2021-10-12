from rest_framework import serializers

from .models import Task


class TaskListSerializers(serializers.ModelSerializer):
    """Список заданий"""
    class Meta:
        model = Task
        fields = ('id', 'content', 'status', 'published')


class TaskDetailSerializers(serializers.ModelSerializer):
    """Задание"""
    class Meta:
        model = Task
        fields = '__all__'
