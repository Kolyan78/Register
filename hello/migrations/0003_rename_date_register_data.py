# Generated by Django 4.2a1 on 2023-02-12 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_remove_register_client_remove_register_master'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='date',
            new_name='data',
        ),
    ]
