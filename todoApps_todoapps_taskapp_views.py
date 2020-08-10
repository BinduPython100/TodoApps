from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import SignUpForm, TaskForm
from .forms import TaskForms
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


class LoginView(LoginView):
    redirect_authenticated_user = True


def index_view(request):
    form = TaskForm.objects.all()
    return render(request, 'taskapp/index.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logout successfully")
    return redirect("/")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'taskapp/signup.html', {'form': form})


@login_required(login_url='/login')
def task_view(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = TaskForms()
    return render(request, 'taskapp/task.html', {'form': form})


@login_required(login_url='/login')
def post_update(request, id):
    post = get_object_or_404(TaskForm, id=id)
    if post.author == request.user:
        form = TaskForms(request.POST or None, instance=post)
        context = {'form': form}
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "You successfully updated the post")
            context = {'form': form}
            return redirect('/')
        else:
            context = {'form': form, }
            return render(request, 'taskapp/taskupdate.html', context)
    else:
        messages.success(request, "You cannot have access to updated the post")
        return redirect('/')


@login_required(login_url='/login')
def post_delete(request, id):
    post = get_object_or_404(TaskForm, id=id)
    post = TaskForm.objects.get(id=id)
    post.delete()
    messages.info(request, 'Your post is delete successfully!')
    return redirect('index')
