from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task, Tag
from .forms import TaskForm, TaskSearchForm, TagForm, TagSearchForm

# TASK Views

@login_required
def task_index(request):
    """View function for the Task home page."""
    num_tasks = Task.objects.count()
    tasks_not_done = Task.objects.filter(is_done=False).count()
    tasks_done = Task.objects.filter(is_done=True).count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tasks": num_tasks,
        "tasks_not_done": tasks_not_done,
        "tasks_done": tasks_done,
        "num_visits": num_visits + 1,
    }

    return render(request, "task/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "task/task_list.html"
    context_object_name = "task_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("content", "")
        context["search_form"] = TaskSearchForm(initial={"content": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.order_by('is_done', '-datetime')
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(content__icontains=form.cleaned_data["content"])

        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "task/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_confirm_delete.html"


@login_required
def toggle_task_status(request, pk):
    """Toggle the status of a Task."""
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tasks:task-list")

# TAG Views

class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5
    template_name = "task/tag_list.html"
    context_object_name = "tag_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TagSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Tag.objects.all()
        form = TagSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag
    template_name = "task/tag_detail.html"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")
    template_name = "task/tag_form.html"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")
    template_name = "task/tag_form.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
    template_name = "task/tag_confirm_delete.html"
