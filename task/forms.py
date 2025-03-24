from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "datetime", "deadline", "is_done", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "Describe your task here...", "rows": 3}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TaskSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by task content",
            }
        )
    )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter tag name"}),
        }


class TagSearchForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by tag name",
            }
        )
    )
