# Generated by Django 3.2.8 on 2021-11-15 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='keyword_id',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.CharField(default='abc', max_length=10000),
        ),
        migrations.AddField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='keyword_name',
            field=models.CharField(default='abc', max_length=255),
            preserve_default=False,
        ),
    ]
