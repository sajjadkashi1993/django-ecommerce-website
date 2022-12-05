# Generated by Django 4.1.3 on 2022-12-05 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profileuser_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(error_messages={'unique': 'A user with that phone already exists.'}, help_text='Required. 11 character. digits only.', max_length=11, unique=True, verbose_name='phone number')),
                ('code', models.CharField(max_length=8)),
                ('number_try', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(default='iran', max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('adderess', models.TextField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='accounts.profileuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
