# Generated by Django 4.2a1 on 2023-02-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='client',
        ),
        migrations.RemoveField(
            model_name='register',
            name='master',
        ),
    ]
