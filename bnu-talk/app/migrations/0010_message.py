# Generated by Django 3.2.8 on 2021-11-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_keyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_user_id', models.IntegerField()),
                ('receive_user_id', models.IntegerField()),
            ],
        ),
    ]
