"""
THis file constains viewset for employee model for possibility of CRUD procedures.
"""

from rest_framework import viewsets

from ..rest.serializers import EmployeeSerializer
from ..models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    This class realized viewset for serializing of employee model.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
