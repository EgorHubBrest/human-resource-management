from rest_framework import viewsets

from ..rest.serializers import EmployeeSerializer
from ..models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
