# Written by developer. Inserting test data

from django.db import migrations


def forward_insert_data(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Employee = apps.get_model('department_app', 'Employee')

    Department.objects.bulk_create([
        Department(name='Development'),
        Department(name='Testing'),
        Department(name='Finance'),
    ])

    dep_dev = Department.objects.get(name='Development')

    dep_dev.employee_set.bulk_create([
        Employee(name='Renee Stokes', date_of_birth='1997-04-26', salary=1500.0, related_department=dep_dev),
        Employee(name='Abbi Finch', date_of_birth='1993-09-04', salary=3500.0, related_department=dep_dev),
    ])

    dep_fin = Department.objects.get(name='Finance')
    dep_fin.employee_set.bulk_create([
        Employee(name='Ahmet Hayes', date_of_birth='1994-02-19', salary=1100.0, related_department=dep_fin),
        Employee(name='Kaylegh Pineda', date_of_birth='1999-07-29', salary=800.0, related_department=dep_fin),
    ])

    dep_test = Department.objects.get(name='Testing')
    dep_test.employee_set.bulk_create([
        Employee(name='Almie Patel', date_of_birth='1995-11-12', salary=1000.0, related_department=dep_test),
        Employee(name='Neo Tumbull', date_of_birth='1995-11-12', salary=1000.0, related_department=dep_test),
    ])


def backward_delete_data(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Employee = apps.get_model('department_app', 'Employee')

    Employee.objects.all().delete()
    Department.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('department_app',
         '0001_initial',
         ),
    ]

    operations = [
        migrations.RunPython(forward_insert_data, backward_delete_data),
    ]
