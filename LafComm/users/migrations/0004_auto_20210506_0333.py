# Generated by Django 3.1.7 on 2021-05-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210506_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_year',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ManyToManyField(blank=True, to='users.Department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='interest_newsletter',
            field=models.ManyToManyField(blank=True, to='users.NewsletterSection'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='relation_to_college',
            field=models.CharField(choices=[('Student', 'Student'), ('Alumni', 'Alumni'), ('Faculty', 'Faculty'), ('Staff', 'Staff'), ('Par_Fam', 'Parent/Family'), ('CHC', 'College Hill Community'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]