# Generated by Django 2.1.5 on 2019-01-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190119_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
    ]
