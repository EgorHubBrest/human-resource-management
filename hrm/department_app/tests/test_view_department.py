from django.test import TestCase, Client
from django.utils.http import urlencode
from ..models.department import Department
from rest_framework.reverse import reverse
from rest_framework import status
from django.forms.models import model_to_dict


class TestViewDepartment(TestCase):

    def setUp(self):
        self.client = Client()
        self.department_data = {
            "name": "Test Department",
        }
        self.expected_keys = {key.name for key in Department._meta.fields}
        self.department = Department.objects.create(name="Old Test Department")

    def test_department_create(self):
        """
        Test POST request for REST API
        """
        department_count = Department.objects.count()
        response = self.client.post(reverse('department-list'), data=self.department_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), department_count + 1)
        self.assertEqual(response.data.keys(), self.expected_keys)
        self.assertEqual(response.data, model_to_dict(Department.objects.get(name=self.department_data['name']),
                                                                            fields=self.expected_keys))

    def test_department_read(self):
        """
        Test GET request for REST API
        """
        department_count = Department.objects.count()
        response = self.client.get(reverse('department-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), department_count)
        if department_count > 0:
            self.assertEqual(response.data[0].keys(), self.expected_keys)

    def test_department_update(self):
        """
        Test UPDATE request for REST API
        """
        department_count = Department.objects.count()
        response = self.client.put(reverse('department-detail', args=(self.department.id,)),
                                   data=urlencode(self.department_data),
                                   content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Department.objects.count(), department_count)
        self.assertEqual(response.data.keys(), self.expected_keys)
        self.assertEqual(response.data, model_to_dict(Department.objects.get(id=self.department.id),
                                                      fields=self.expected_keys))
        self.assertEqual(Department.objects.get(id=self.department.id).name, self.department_data["name"])

    def test_department_delete(self):
        """
        Test DELETE request for REST API
        """
        department_count = Department.objects.count()
        response = self.client.delete(reverse('department-detail', args=(self.department.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), department_count - 1)
