from django.urls import path
from .views import TaskListCreateView, TaskDeleteView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    
    path('<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]