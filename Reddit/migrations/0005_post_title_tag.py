# Generated by Django 4.1.4 on 2022-12-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0004_rename_auto_increment_id_post_id_post_remove_post_zz'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Reddit', max_length=255),
        ),
    ]
