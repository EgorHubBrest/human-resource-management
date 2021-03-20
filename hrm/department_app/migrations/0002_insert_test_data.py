# Written by developer. Inserting test data

from django.db import migrations


def insert_data(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    dep_dev = Department(name='Development')
    dep_dev.save()
    dep_test = Department(name='Testing')
    dep_test.save()
    dep_fin = Department(name='Finance')
    dep_fin.save()
    dep_dev.employee_set.create(name='Renee Stokes', date_of_birth='1997-04-26', salary=1500.0)
    dep_dev.employee_set.create(name='Abbi Finch', date_of_birth='1993-09-04', salary=3500.0)
    dep_fin.employee_set.create(name='Ahmet Hayes', date_of_birth='1994-02-19', salary=1100.0)
    dep_fin.employee_set.create(name='Kaylegh Pineda', date_of_birth='1999-07-29', salary=800.0)
    dep_test.employee_set.create(name='Almie Patel', date_of_birth='1995-11-12', salary=1000.0)
    dep_test.employee_set.create(name='Neo Tumbull', date_of_birth='1995-11-12', salary=1000.0)


class Migration(migrations.Migration):

    dependencies = [
        ('department_app',
         '0001_initial',
         ),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]
