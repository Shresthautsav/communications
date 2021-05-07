# Generated by Django 3.1.7 on 2021-04-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('preferred_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('Student', 'Student'), ('Alumni', 'Alumni'), ('Faculty', 'Faculty'), ('Staff', 'Staff'), ('Parent', 'Parent'), ('Friends of College', 'Friends of College')], max_length=20)),
                ('class_of', models.CharField(max_length=10)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]