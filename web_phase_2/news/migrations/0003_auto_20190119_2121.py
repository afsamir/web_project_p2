# Generated by Django 2.1.5 on 2019-01-19 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('date',)},
        ),
    ]
