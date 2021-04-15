"""
Information about Department model.
"""

from django.db import models


class Department(models.Model):
    """
    This is a class implementation of model department in Django ORM.
    """

    name = models.CharField(max_length=70, unique=True)
