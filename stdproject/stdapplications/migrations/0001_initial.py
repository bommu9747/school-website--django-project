# Generated by Django 3.2.15 on 2023-01-25 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='viewexamlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('messages', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('department', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('conform', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('years', models.IntegerField()),
                ('status', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('department', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('conform', models.CharField(max_length=250)),
                ('years', models.IntegerField()),
                ('status', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('reason', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('department', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('conform', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('years', models.IntegerField()),
                ('status', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
