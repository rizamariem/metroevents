# Generated by Django 3.1.1 on 2021-03-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteroEvents', '0006_auto_20210321_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobileNum',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
    ]