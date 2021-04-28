from django.test import TestCase, Client
from ..models.department import Department
from rest_framework.reverse import reverse


class TestViewDepartment(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_department(self):
        response = self.client.get(reverse('department-list', format='json'))
        self.assertEqual(response.status_code, 200)

    def test_create_department(self):
        dep = Department.objects.create(name='NewTestDepartment')
        response = self.client.get('/department/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, dep.name)
