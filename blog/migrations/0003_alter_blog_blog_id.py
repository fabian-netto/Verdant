# Generated by Django 4.0.4 on 2022-04-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
