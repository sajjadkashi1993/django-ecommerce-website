# Generated by Django 4.1.3 on 2022-12-07 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='type',
            field=models.IntegerField(choices=[(1, 'Percent'), (2, 'Amount')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
