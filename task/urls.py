from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    path("", views.task_index, name="index"),
    path("task/list/", views.TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/detail/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle-status/", views.toggle_task_status, name="task-toggle-status"),
    path("tag/list/", views.TagListView.as_view(), name="tag-list"),
    path("tag/<int:pk>/detail/", views.TagDetailView.as_view(), name="tag-detail"),
    path("tag/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]
