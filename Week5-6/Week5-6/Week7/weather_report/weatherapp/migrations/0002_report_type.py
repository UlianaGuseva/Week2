# Generated by Django 4.2 on 2023-05-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(blank=True, choices=[('sunny', 'Sunny'), ('cloudy', 'Cloudy'), ('windy', 'Windy'), ('rainy', 'Rainy'), ('stormy', 'Stormy')], max_length=10, null=True),
        ),
    ]
