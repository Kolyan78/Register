# Generated by Django 4.2a1 on 2023-03-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0011_alter_master_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
