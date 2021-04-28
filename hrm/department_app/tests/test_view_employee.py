from django.test import TestCase, Client
from ..models.employee import Employee
from ..models.department import Department
from datetime import datetime
from dateutil.relativedelta import relativedelta


class TestViewEmployee(TestCase):

    def setUp(self):
        self.client = Client()

