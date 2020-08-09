from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.

priority_tasks = (('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class TaskForm(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    choice = models.CharField(max_length=30, choices=priority_tasks, null=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
