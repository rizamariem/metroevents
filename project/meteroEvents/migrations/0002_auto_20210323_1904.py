# Generated by Django 3.1.1 on 2021-03-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meteroEvents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='event_type',
            new_name='etype',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='event_name',
            new_name='name',
        ),
    ]
