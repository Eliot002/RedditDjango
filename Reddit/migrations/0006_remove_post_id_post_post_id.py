# Generated by Django 4.1.4 on 2022-12-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0005_post_title_tag'),
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
