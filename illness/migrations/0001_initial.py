# Generated by Django 3.1.5 on 2021-01-24 15:21

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icd10_code', models.CharField(blank=True, max_length=300, null=True)),
                ('cluster', models.IntegerField(null=True)),
                ('criticality', models.IntegerField(null=True)),
                ('active', models.BooleanField(null=True)),
                ('dfstatus', models.CharField(blank=True, max_length=300, null=True)),
                ('source', models.CharField(blank=True, max_length=300, null=True)),
                ('groups_complete', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('version', models.IntegerField(null=True)),
                ('prevalence', models.IntegerField(null=True)),
                ('prior', models.FloatField(null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('mergedVersions', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), blank=True, null=True, size=None)),
                ('state', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]