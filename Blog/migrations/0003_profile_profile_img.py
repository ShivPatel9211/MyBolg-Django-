# Generated by Django 3.1.7 on 2021-03-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210303_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]