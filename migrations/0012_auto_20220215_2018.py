# Generated by Django 3.2.8 on 2022-02-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mino', '0011_work1_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subimage',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='サブ画像'),
        ),
        migrations.AddField(
            model_name='profile',
            name='topimage',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='トップ画像'),
        ),
    ]
