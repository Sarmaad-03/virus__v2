# Generated by Django 5.0.1 on 2024-02-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_emp',
            field=models.BooleanField(default=True),
        ),
    ]
