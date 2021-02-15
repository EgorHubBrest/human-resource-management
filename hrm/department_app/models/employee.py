from django.db import models
from .department import Department


class Employee(models.Model):
    related_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    salary = models.FloatField()
