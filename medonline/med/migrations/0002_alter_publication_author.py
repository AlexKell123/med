# Generated by Django 5.0 on 2023-12-13 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='med.doctor'),
        ),
    ]
