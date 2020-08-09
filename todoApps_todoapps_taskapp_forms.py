from django import forms
from .models import TaskForm


class TaskForms(forms.ModelForm):
    class Meta:
        model = TaskForm
        fields = '__all__'
