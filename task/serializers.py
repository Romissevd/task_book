from rest_framework import serializers

from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['title', 'text', 'author', 'performer', 'image']


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class TaskEditSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
