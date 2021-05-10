from django.test import TestCase, Client
from ..models.employee import Employee
from ..models.department import Department
import datetime
from rest_framework.reverse import reverse
from rest_framework import status
from django.utils.http import urlencode
from django.forms.models import model_to_dict


class TestViewEmployee(TestCase):

    def setUp(self):
        self.client = Client()
        self.expected_keys = {key.name for key in Employee._meta.fields}
        self.department = Department.objects.create(name="Test Department")
        self.employee = Employee.objects.create(name="Old Test Employee", salary=1000.0,
                                                date_of_birth=datetime.datetime(year=2000, month=9, day=9).strftime("%Y-%m-%d"),
                                                related_department=self.department)
        self.employee_data = {
            "name": "Test Employee",
            "date_of_birth": datetime.datetime(year=1999, month=9, day=9).strftime("%Y-%m-%d"),
            "salary": 1000.0,
            "related_department": self.department.id
        }

    def test_employee_create(self):
        """
        Test POST request for REST API
        """
        employee_count = Employee.objects.count()
        response = self.client.post(reverse('employee-list'), data=self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), employee_count + 1)
        self.assertEqual(response.data.keys(), self.expected_keys)
        new_emp_dict = model_to_dict(Employee.objects.get(name=self.employee_data['name']), fields=self.expected_keys)
        for field in self.expected_keys:
            if isinstance(new_emp_dict[field], datetime.date):
                self.assertEqual(response.data[field], new_emp_dict[field].strftime("%Y-%m-%d"))
            else:
                self.assertEqual(response.data[field], new_emp_dict[field])

    def test_employee_read(self):
        """
        Test GET request for REST API
        """
        employee_count = Employee.objects.count()
        response = self.client.get(reverse('employee-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), employee_count)
        if employee_count > 0:
            self.assertEqual(response.data[0].keys(), self.expected_keys)

    def test_employee_update(self):
        """
        Test UPDATE request for REST API
        """
        employee_count = Employee.objects.count()
        response = self.client.put(reverse('employee-detail', args=(self.employee.id,)),
                                   data=urlencode(self.employee_data),
                                   content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), employee_count)
        self.assertEqual(response.data.keys(), self.expected_keys)
        new_emp_dict = model_to_dict(Employee.objects.get(id=self.employee.id), fields=self.expected_keys)
        for field in self.expected_keys:
            if isinstance(new_emp_dict[field], datetime.date):
                self.assertEqual(response.data[field], new_emp_dict[field].strftime("%Y-%m-%d"))
            else:
                self.assertEqual(response.data[field], new_emp_dict[field])
        self.assertEqual(new_emp_dict["name"], self.employee_data["name"])

    def test_employee_delete(self):
        """
        Test DELETE request for REST API
        """
        employee_count = Employee.objects.count()
        response = self.client.delete(reverse('employee-detail', args=(self.employee.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), employee_count - 1)

    def test_create_more_th_max_length(self):
        employee_count = Employee.objects.count()
        big_emp = {
            "name": "Very very very very very very very very very very "
                    "very very very very very very very very very big name",
            "date_of_birth": datetime.datetime(year=1999, month=9, day=9).strftime("%Y-%m-%d"),
            "salary": 1000.0,
            "related_department": self.department.id
        }
        max_length = Employee._meta.get_field('name').max_length
        response = self.client.post(reverse('employee-list'), data=big_emp, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0], f'Ensure this field has no more than {max_length} characters.')
        self.assertEqual(response.data['name'][0].code, 'max_length')
        self.assertEqual(Employee.objects.count(), employee_count)

    def test_update_more_th_max_length(self):
        employee_count = Employee.objects.count()
        big_emp = {
            "name": "Very very very very very very very very very very "
                    "very very very very very very very very very big name",
            "date_of_birth": datetime.datetime(year=1999, month=9, day=9).strftime("%Y-%m-%d"),
            "salary": 1000.0,
            "related_department": self.department.id
        }
        max_length = Employee._meta.get_field('name').max_length
        response = self.client.put(reverse('employee-detail', args=(self.employee.id,)),
                                   data=urlencode(big_emp),
                                   content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0], f'Ensure this field has no more than {max_length} characters.')
        self.assertEqual(response.data['name'][0].code, 'max_length')
        self.assertEqual(Employee.objects.count(), employee_count)

    def test_cascade_delete(self):
        employee_count = Employee.objects.count()
        department_count = Department.objects.count()
        count_emp_to_rmv = len(Employee.objects.filter(related_department_id=self.department.id))
        response = self.client.delete(reverse('department-detail', args=(self.department.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), department_count - 1)
        self.assertEqual(Employee.objects.count(), employee_count - count_emp_to_rmv)
