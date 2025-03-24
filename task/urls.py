from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    path("", views.task_index, name="index"),
    path("list/", views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/detail/", views.TaskDetailView.as_view(), name="task-detail"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/toggle-status/", views.toggle_task_status, name="task-toggle-status"),
    path("list/", views.TagListView.as_view(), name="tag-list"),
    path("<int:pk>/detail/", views.TagDetailView.as_view(), name="tag-detail"),
    path("create/", views.TagCreateView.as_view(), name="tag-create"),
    path("<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]
