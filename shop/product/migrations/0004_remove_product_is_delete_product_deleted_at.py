# Generated by Django 4.1.3 on 2022-12-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_delete',
        ),
        migrations.AddField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
