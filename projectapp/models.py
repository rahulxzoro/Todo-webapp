from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.TextField()
    date=models.DateField()
    
    def __str__(self) :
        return self.task