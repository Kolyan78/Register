# Generated by Django 4.2a1 on 2023-03-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_alter_register_client_alter_register_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
