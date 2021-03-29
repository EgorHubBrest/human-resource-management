"""
Information about Department model.
"""
from django.db import models


class Department(models.Model):
    """
    Department model implementation.
    """
    name = models.CharField(max_length=70)
