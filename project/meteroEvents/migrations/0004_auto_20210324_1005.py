# Generated by Django 3.1.1 on 2021-03-24 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meteroEvents', '0003_auto_20210324_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requesttoorg',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='requesttopart',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Requesttoadmin',
        ),
        migrations.DeleteModel(
            name='Requesttoorg',
        ),
        migrations.DeleteModel(
            name='Requesttopart',
        ),
    ]
