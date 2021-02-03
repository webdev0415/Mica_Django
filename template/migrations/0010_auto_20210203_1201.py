# Generated by Django 3.1.5 on 2021-02-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0009_auto_20210203_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valuestore',
            old_name='es_kiosk_name',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='valuestore',
            old_name='kiosk_name',
            new_name='es_name',
        ),
        migrations.RenameField(
            model_name='valuestore',
            old_name='value',
            new_name='name',
        ),
        migrations.AddField(
            model_name='valuestore',
            name='old_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]