# Generated by Django 4.1.3 on 2022-12-12 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_image_galery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='galery', to='product.product', verbose_name='product'),
        ),
    ]
