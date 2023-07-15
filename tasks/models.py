from django.db import models
from django.utils.timezone import now
from django.urls import reverse_lazy


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    deadline = models.DateField(default=now)
    created_at = models.DateField(auto_now_add=True)
    is_done = models.BooleanField()

    def get_absolute_url(self):
        return reverse_lazy('tasks:all_tasks')
