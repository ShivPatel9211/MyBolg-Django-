# Generated by Django 3.1.7 on 2021-05-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_auto_20210501_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Computer Engineering', max_length=100)),
            ],
        ),
    ]
