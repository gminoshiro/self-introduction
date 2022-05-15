# Generated by Django 3.2.8 on 2022-02-13 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mino', '0009_software_technical'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='period',
        ),
        migrations.RemoveField(
            model_name='technical',
            name='period',
        ),
        migrations.AlterField(
            model_name='software',
            name='percentage',
            field=models.IntegerField(verbose_name='パーセンテージ'),
        ),
        migrations.AlterField(
            model_name='technical',
            name='percentage',
            field=models.IntegerField(verbose_name='パーセンテージ'),
        ),
    ]
