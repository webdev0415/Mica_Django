# Generated by Django 3.1.5 on 2021-01-12 19:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataKeyStore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('es_title', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('section_name', models.CharField(blank=True, max_length=300, null=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.category')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('multiple_values', models.CharField(blank=True, max_length=300, null=True)),
                ('criticality', models.IntegerField()),
                ('treatable', models.BooleanField()),
                ('prior', models.DecimalField(decimal_places=2, max_digits=5)),
                ('question', models.CharField(blank=True, max_length=300, null=True)),
                ('es_question', models.CharField(blank=True, max_length=300, null=True)),
                ('antithesis', models.FloatField()),
                ('sub_groups', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('bodyparts', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('pain_swelling_id', models.IntegerField()),
                ('display_order', models.IntegerField(default=0)),
                ('icd_r_odes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('display_ymptom', models.BooleanField()),
                ('kiosk_name', models.CharField(blank=True, max_length=300, null=True)),
                ('formal_name', models.CharField(blank=True, max_length=300, null=True)),
                ('med_necessary', models.BooleanField()),
                ('min_diag_criteria', models.BooleanField()),
                ('display_dr_app', models.BooleanField()),
                ('gender_group', models.CharField(blank=True, max_length=300, null=True)),
                ('cardinality', models.BooleanField()),
                ('logical_group_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('de_groups', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('symptom_type', models.CharField(blank=True, max_length=300, null=True)),
                ('time_type', models.TimeField()),
                ('min_range', models.FloatField()),
                ('max_range', models.FloatField()),
                ('is_range', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SymptomsTmpl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bias', models.BooleanField()),
                ('range_values', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=5), size=None)),
                ('descriptors', models.CharField(blank=True, max_length=300, null=True)),
                ('descriptor_file', models.CharField(blank=True, max_length=300, null=True)),
                ('question_text', models.CharField(blank=True, max_length=300, null=True)),
                ('scale_info_text', models.CharField(blank=True, max_length=300, null=True)),
                ('scale_time_limit', models.IntegerField()),
                ('scale_time_limit_start', models.IntegerField()),
                ('time_unit_default', models.IntegerField()),
                ('datastore_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=300, null=True), size=None)),
                ('criticality', models.IntegerField()),
                ('treatable', models.BooleanField()),
                ('prior', models.FloatField()),
                ('question', models.CharField(blank=True, max_length=300, null=True)),
                ('es_question', models.CharField(blank=True, max_length=300, null=True)),
                ('antithesis', models.FloatField()),
                ('display_symptom', models.BooleanField()),
                ('med_necessary', models.BooleanField()),
                ('min_diag_criteria', models.BooleanField()),
                ('display_dr_app', models.BooleanField()),
                ('gender_group', models.CharField(blank=True, max_length=300, null=True)),
                ('time_type', models.TimeField()),
                ('min_range', models.FloatField()),
                ('max_range', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ValueStore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('m_antithesis', models.FloatField()),
                ('m_icd10Rcode', models.CharField(blank=True, max_length=300, null=True)),
                ('count', models.IntegerField()),
                ('displayListValue', models.BooleanField()),
                ('kiosk_name', models.CharField(blank=True, max_length=300, null=True)),
                ('es_kiosk_name', models.CharField(blank=True, max_length=300, null=True)),
                ('display_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SymptomGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.category')),
                ('datastore_ref_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.datakeystore')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.section')),
            ],
        ),
        migrations.AddField(
            model_name='datakeystore',
            name='values',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.valuestore'),
        ),
        migrations.AddField(
            model_name='category',
            name='symptoms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.symptom'),
        ),
    ]
