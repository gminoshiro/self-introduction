# Generated by Django 3.2.8 on 2022-02-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mino', '0017_auto_20220215_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work1',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='subimage',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='サブ画像'),
        ),
    ]
