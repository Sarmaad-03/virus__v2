# Generated by Django 5.0.1 on 2024-03-06 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_purchase_parfume'),
        ('parfume', '0012_alter_parfume_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='parfume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='parfume.parfume_volume'),
        ),
    ]
