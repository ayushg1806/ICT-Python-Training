from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
