# Generated by Django 4.1.3 on 2022-12-09 20:26

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'adresses'},
        ),
        migrations.AlterModelOptions(
            name='otpcode',
            options={'verbose_name': 'OTP Code', 'verbose_name_plural': 'OTP Codes'},
        ),
        migrations.AlterModelOptions(
            name='profileuser',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AlterField(
            model_name='address',
            name='adderess',
            field=models.TextField(max_length=100, verbose_name='adderess'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='iran', max_length=100, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='postal code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(max_length=100, verbose_name='province'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.CharField(max_length=8, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='number_try',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='number try'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='phone',
            field=models.CharField(error_messages={'unique': 'A user with that phone already exists.'}, help_text='Required. 11 character. digits only.', max_length=11, unique=True, validators=[core.validators.PhoneValidator()], verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(0, 'User'), (1, 'Customer'), (2, 'Admin'), (3, 'Employee')], default=0, max_length=20, verbose_name='role'),
        ),
    ]
