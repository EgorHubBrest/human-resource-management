from django.test import TestCase, Client
from ..models.employee import Employee
from ..models.department import Department
from datetime import datetime


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(name='NewEmployee', date_of_birth=datetime.today(), salary=1000.0,
                                related_department=Department.objects.create(name='NewTestDepartment'))

    def test_object_creation(self):
        test_emp = Employee.objects.create(name='TestEmp', date_of_birth=datetime.today(), salary=1000.0,
                                related_department=Department.objects.get(name='NewTestDepartment'))
        self.assertTrue(isinstance(test_emp, Employee))

    def test_length_of_name_emp(self):
        emp = Employee.objects.get(name='NewEmployee')
        self.assertLessEqual(len(emp.name), emp._meta.get_field('name').max_length)

    def test_max_length(self):
        dep = Employee.objects.get(name='NewEmployee')
        self.assertLessEqual(dep._meta.get_field('name').max_length, 100)
