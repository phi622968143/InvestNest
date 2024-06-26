# Generated by Django 5.0.6 on 2024-05-18 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('PID', models.CharField(max_length=20)),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('Age', models.IntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(120)])),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
