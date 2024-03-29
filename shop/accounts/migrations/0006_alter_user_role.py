# Generated by Django 4.1.3 on 2022-12-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(0, 'User'), (1, 'Customer'), (2, 'Product Manager'), (3, 'Supervisor'), (4, 'Operator')], default=0, max_length=20, verbose_name='role'),
        ),
    ]
