# Generated by Django 4.1.3 on 2022-12-09 20:26

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_content_alter_transaction_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='receiver_mobile',
            field=models.CharField(max_length=15, validators=[core.validators.PhoneValidator()]),
        ),
    ]