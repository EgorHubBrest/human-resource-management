"""
THis file constains viewset for department model for possibility of CRUD procedures.
"""

from rest_framework import viewsets

from ..rest.serializers import DepartmentSerializer
from ..models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    This class realized viewset for serializing of department model.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
