from django.db import models

class Todo(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    status=models.CharField(max_length=18)
