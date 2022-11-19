from django.urls import path
from tasks.views import taskList, yourname, taskView, taskAdd, updateTask, deleteTask

urlpatterns = [
    path('', taskList, name='list'),
    path('task/<int:id>', taskView, name='url_task-view'),
    path('task-add/', taskAdd, name='url_task-add'),
    path('yourname/<str:nome>', yourname),
    path('update-task/<int:id>', updateTask, name='url_update-task'),
    path('task-delete/<int:id>', deleteTask, name='url_delete-task'),
]
