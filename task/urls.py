from django.urls import path
from .views import TaskCreateView, TaskListView, TaskEditorView

urlpatterns = [
    path('task/create/', TaskCreateView.as_view()),
    path('task/list/', TaskListView.as_view()),
    path('task/edit/<int:pk>/', TaskEditorView.as_view()),
]