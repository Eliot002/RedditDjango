# Generated by Django 4.1.4 on 2023-02-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0020_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
