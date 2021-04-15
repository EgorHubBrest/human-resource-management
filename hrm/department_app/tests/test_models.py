from django.test import TestCase
from ..models.department import Department
from django.db.utils import IntegrityError


class DepartmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Department.objects.create(name='NewTestDepartment')

    def test_length_of_departments(self):
        dep = Department.objects.get(name='NewTestDepartment')
        self.assertLessEqual(len(dep.name), dep._meta.get_field('name').max_length)

    def test_max_length(self):
        dep = Department.objects.get(name='NewTestDepartment')
        self.assertLessEqual(dep._meta.get_field('name').max_length, 70)

    def test_adding_existing(self):
        try:
            Department.objects.create(name='Finance')
        finally:
            self.assertRaises(IntegrityError)

    def test_name_is_unique(self):
        dep = Department.objects.get(name='NewTestDepartment')
        yet_in_db = False
        for exist_dep in Department.objects.all():
            if dep.name == exist_dep.name and not yet_in_db:
                yet_in_db = True
                continue
            self.assertNotEqual(dep.name, exist_dep.name)
