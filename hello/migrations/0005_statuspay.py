# Generated by Django 4.2a1 on 2023-03-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_delete_statuspay_rename_data_register_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]