# Generated by Django 3.0.4 on 2020-04-25 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_amazon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='new_field',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_ptr_id',
        ),
    ]