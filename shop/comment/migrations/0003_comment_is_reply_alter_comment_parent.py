# Generated by Django 4.1.3 on 2022-12-19 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_options_alter_comment_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comment.comment', verbose_name='parent'),
        ),
    ]
