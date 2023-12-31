# Generated by Django 4.2.3 on 2023-08-09 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('fees', models.FloatField(max_length=200)),
                ('comment', models.TextField()),
                ('duration', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('semail', models.CharField(max_length=200)),
                ('sphone', models.IntegerField()),
                ('scollege', models.CharField(max_length=200)),
                ('sdegree', models.CharField(max_length=200)),
                ('total_amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('due_amount', models.FloatField()),
                ('scourses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
            ],
        ),
    ]
