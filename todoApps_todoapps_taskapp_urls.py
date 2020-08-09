from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout', views.logout_view, name="logout"),
    path('task/', views.task_view, name="task_view"),
    path('post_update/<int:id>', views.post_update, name="post_update"),
    path('post_delete/<int:id>', views.post_delete, name="post_delete")
]
