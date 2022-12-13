# Generated by Django 4.1.3 on 2022-12-13 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_price_options_remove_image_gallery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.gallery', verbose_name='galery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image1',
            field=models.ImageField(upload_to='image/', verbose_name='image_109x122'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image2',
            field=models.ImageField(upload_to='image/', verbose_name='image_580x900'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image3',
            field=models.ImageField(upload_to='image/', verbose_name='image_800x900'),
        ),
    ]
