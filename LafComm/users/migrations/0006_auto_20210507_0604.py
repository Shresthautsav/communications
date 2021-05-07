# Generated by Django 3.1.7 on 2021-05-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210507_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='relation_to_college',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Alumni', 'Alumni'), ('Faculty', 'Faculty'), ('Staff', 'Staff'), ('Par_Fam', 'Parent/Family'), ('CHC', 'College Hill Community'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
