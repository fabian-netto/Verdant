# Generated by Django 4.0.4 on 2022-04-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000)),
                ('img_main', models.ImageField(upload_to='')),
                ('img_1', models.ImageField(upload_to='')),
                ('img_2', models.ImageField(upload_to='')),
                ('img_3', models.ImageField(upload_to='')),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]