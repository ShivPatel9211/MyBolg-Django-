# Generated by Django 3.1.7 on 2021-05-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_post_caty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]