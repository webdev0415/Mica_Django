# Generated by Django 3.1.5 on 2021-02-03 00:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0003_auto_20210202_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmenttyperefdesc',
            name='concept_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]