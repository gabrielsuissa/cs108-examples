# Generated by Django 3.0.4 on 2020-04-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_amazon', '0004_auto_20200424_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(blank=True),
        ),
    ]