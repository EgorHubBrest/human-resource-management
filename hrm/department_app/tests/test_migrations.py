from django.apps import apps
from django.test import TestCase, Client
from django.db.migrations.executor import MigrationExecutor
from django.db import connection


class TestMigrations(TestCase):

    @property
    def app(self):
        return apps.get_containing_app_config(type(self).__module__).name

    migrate_from = None
    migrate_to = None

    def setUp(self):
        assert self.migrate_from and self.migrate_to, \
            "TestCase '{}' must define migrate_from and migrate_to properties".format(type(self).__name__)
        self.migrate_from = [(self.app, self.migrate_from)]
        self.migrate_to = [(self.app, self.migrate_to)]
        executor = MigrationExecutor(connection)
        old_apps = executor.loader.project_state(self.migrate_from).apps

        executor.migrate(self.migrate_from)
        self.setUpBeforeMigration(old_apps)

        executor = MigrationExecutor(connection)
        executor.loader.build_graph()  # reload.
        executor.migrate(self.migrate_to)

        self.apps = executor.loader.project_state(self.migrate_to).apps

    def setUpBeforeMigration(self, apps):
        pass


class TestInsertingData(TestMigrations):
    migrate_from = '0001_initial'
    migrate_to = '0002_insert_test_data'

    def setUpBeforeMigration(self, apps):
        self.client = Client()
        response_dep = self.client.get('/department/')
        self.assertNotContains(response_dep, 'Development')
        response_emp = self.client.get('/employee/')
        self.assertNotContains(response_emp, 'Renee Stokes')

    def test_inserting_data(self):
        response_dep = self.client.get('/department/')
        self.assertContains(response_dep, 'Development')
        response_emp = self.client.get('/employee/')
        self.assertContains(response_emp, 'Renee Stokes')