"""
Information about Employee model.
"""

from django.db import models
from .department import Department


class Employee(models.Model):
    """
    This is a class implementation of model employee in Django ORM.
    """

    related_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    salary = models.FloatField()
