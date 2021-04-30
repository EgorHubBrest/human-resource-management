"""
This file contains serializers for sending necessary information to users in format JSON.
"""

from rest_framework import serializers
from department_app.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    """
    This class is serializer for employee model in Django ORM.
    """
    related_department = serializers.SlugRelatedField(slug_field='id', queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """
    This class is serializer for department model in Django ORM.
    """

    class Meta:
        model = Department
        fields = "__all__"
