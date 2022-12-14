from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS = (('doing', 'Doing'),
             ('done', 'Done')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']



