# Generated by Django 2.2.6 on 2020-02-14 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bb',
            name='product',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
