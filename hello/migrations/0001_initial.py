# Generated by Django 4.2a1 on 2023-02-12 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('rest', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StatusPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('mprice', models.FloatField(default=0)),
                ('ready', models.BooleanField(default=False)),
                ('invoice', models.IntegerField(default=0)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hello.client')),
                ('master', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hello.master')),
            ],
        ),
    ]
