from rest_framework import viewsets

from ..rest.serializers import DepartmentSerializer
from ..models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
