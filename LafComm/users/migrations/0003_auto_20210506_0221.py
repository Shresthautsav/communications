# Generated by Django 3.1.7 on 2021-05-06 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210503_0408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='major_name',
            new_name='major',
        ),
    ]
