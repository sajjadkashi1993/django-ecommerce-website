# Generated by Django 4.1.3 on 2022-12-25 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='status',
        ),
    ]
