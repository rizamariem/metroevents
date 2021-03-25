# Generated by Django 3.1.1 on 2021-03-23 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=45)),
                ('event_name', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=100)),
                ('upvote', models.IntegerField(default=0)),
                ('date_start', models.DateField(auto_now=True)),
                ('date_end', models.DateField(auto_now=True)),
                ('image', models.FileField(blank=True, default='default.jpg', null=True, upload_to='media')),
                ('video', models.FileField(blank=True, default='default.jpg', null=True, upload_to='media')),
                ('cancellation', models.BinaryField(default=0)),
                ('cancellationDate', models.DateField(null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('targetLocation', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('pword', models.CharField(max_length=50, null=True)),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(default='Male', max_length=5)),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=15, null=True)),
                ('country', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('role', models.IntegerField(default=1)),
                ('date_registered', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=100)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Requesttopart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_time', models.TimeField()),
                ('description', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Requesttopart',
            },
        ),
        migrations.CreateModel(
            name='Requesttoorg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_time', models.TimeField()),
                ('description', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Requesttoorg',
            },
        ),
        migrations.CreateModel(
            name='Requesttoadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_time', models.TimeField()),
                ('description', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Requesttoadmin',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_type', models.IntegerField()),
                ('role', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=100)),
                ('req_date', models.DateField(auto_now=True)),
                ('response', models.IntegerField(default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_date', models.DateField(auto_now=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.events')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Participants',
            },
        ),
        migrations.CreateModel(
            name='Organizers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=100)),
                ('notif_type', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.administrator')),
                ('organizer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.organizers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users')),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.AddField(
            model_name='events',
            name='organizer_id',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.organizers'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meteroEvents.users'),
        ),
    ]