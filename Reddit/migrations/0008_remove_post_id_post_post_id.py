# Generated by Django 4.1.4 on 2022-12-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0007_remove_post_id_post_id_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id_post',
        ),
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
