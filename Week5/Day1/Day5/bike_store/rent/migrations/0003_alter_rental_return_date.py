# Generated by Django 4.2 on 2023-04-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
