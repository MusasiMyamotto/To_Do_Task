from django.contrib import admin
from task.models import Task
from users.models import UserConfirmation
# Register your models here.

admin.site.register(Task)
admin.site.register(UserConfirmation)
