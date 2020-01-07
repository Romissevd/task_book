from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskCreateSerializer, TaskListSerializer, TaskEditSerializer
from .models import Task
from user.permissions import IsOwnerOrReadOnly


class TaskCreateView(generics.CreateAPIView):

    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated, )


class TaskListView(generics.ListAPIView):

    serializer_class = TaskListSerializer
    queryset = Task.objects.all()


class TaskEditorView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TaskEditSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
