# Generated by Django 4.1.3 on 2022-12-12 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_image_galery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='galery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.gallery', verbose_name='galery'),
        ),
    ]
