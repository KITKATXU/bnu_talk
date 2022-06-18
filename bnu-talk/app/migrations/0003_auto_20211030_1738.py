# Generated by Django 3.2.8 on 2021-10-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211030_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='like_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='unlike_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='follow_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='post_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='star_num',
            field=models.IntegerField(default=0),
        ),
    ]
