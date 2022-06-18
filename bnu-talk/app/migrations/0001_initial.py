# Generated by Django 3.2.8 on 2021-10-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('content', models.CharField(max_length=10000)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_star',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('follow_id', models.IntegerField()),
                ('star_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('keyword_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=10000)),
                ('like_number', models.IntegerField()),
                ('unlike_number', models.IntegerField()),
                ('comment_number', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('keyword_id', models.IntegerField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unlike',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('follow_num', models.IntegerField()),
                ('star_num', models.IntegerField()),
                ('post_num', models.IntegerField()),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
    ]
