# Generated by Django 3.1.1 on 2020-09-08 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200908_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='subject',
        ),
    ]
