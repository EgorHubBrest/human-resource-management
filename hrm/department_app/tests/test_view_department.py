from django.test import TestCase, Client
from ..models.department import Department


class TestViewDepartment(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_department(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)

    def test_create_department(self):
        dep = Department.objects.create(name='NewTestDepartment')
        response = self.client.get('/department/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, dep.name)
