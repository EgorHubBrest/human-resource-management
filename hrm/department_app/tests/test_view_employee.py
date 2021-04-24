from django.test import TestCase, Client
from ..models.employee import Employee
from ..models.department import Department
from datetime import datetime
from dateutil.relativedelta import relativedelta


class TestViewEmployee(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_employees(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        dep = Department.objects.create(name='NewTestDepartment')
        date_of_birth = datetime.now() - relativedelta(years=18)
        emp = Employee.objects.create(name="Test Employee", salary=1000.0, related_department=dep,
                                      date_of_birth=date_of_birth.strftime("%Y-%m-%d"))
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, emp.name)
