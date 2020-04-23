from django.db import models

# Create your models here.
from dept.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    regON = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
