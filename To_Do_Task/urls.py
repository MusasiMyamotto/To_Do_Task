from django.contrib import admin
from django.urls import path
from task.views import TaskList, TaskDetail
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('login/', AuthorizationAPIView.as_view()),
    path('conf/', ConfirmUserAPIView.as_view()),
]
