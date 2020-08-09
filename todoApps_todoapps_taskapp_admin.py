from django.contrib import admin
from .models import TaskForm


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(TaskForm)
