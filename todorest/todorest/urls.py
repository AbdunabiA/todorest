from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from todoapp.views import TodoListAPIView,TodoCreateAPIView, TodoRetrieveAPIView, TodoDestroyAPIView, TodoUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', TodoListAPIView.as_view(), name='todo-list'),
    path('todo/add', TodoCreateAPIView.as_view(), name='todo-create'),
    path('todoget/<int:pk>', TodoRetrieveAPIView.as_view(), name='todo-retrieve'),
    path('tododel/<int:pk>', TodoDestroyAPIView.as_view(), name='todo-destroy'),
    path('todoput/<int:pk>', TodoUpdateAPIView.as_view(), name='todo-update'),
    path('token/', obtain_auth_token),
]
