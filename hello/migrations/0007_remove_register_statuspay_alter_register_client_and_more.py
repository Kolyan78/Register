# Generated by Django 4.2a1 on 2023-03-27 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_register_statuspay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='statuspay',
        ),
        migrations.AlterField(
            model_name='register',
            name='client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hello.client'),
        ),
        migrations.AlterField(
            model_name='register',
            name='master',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hello.master'),
        ),
    ]
