# Generated by Django 5.1.1 on 2024-09-07 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=36, null=True)),
                ('course_details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers_name', models.CharField(blank=True, max_length=36, null=True)),
                ('teacher_image', models.ImageField(upload_to='teacher')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.details')),
            ],
        ),
    ]
