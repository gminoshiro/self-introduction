# Generated by Django 3.2.8 on 2022-02-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mino', '0006_rename_work_work1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='subimage',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='topimage',
        ),
        migrations.RemoveField(
            model_name='work1',
            name='image',
        ),
    ]
