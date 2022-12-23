# Generated by Django 4.1.3 on 2022-12-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profileuser_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='image',
            field=models.ImageField(blank=True, default='profile/image/agents/3.jpg', null=True, upload_to='profile/', verbose_name='image'),
        ),
    ]