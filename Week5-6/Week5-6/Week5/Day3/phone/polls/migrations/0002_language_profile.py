# Generated by Django 4.2 on 2023-04-24 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counrty_origin', models.CharField(max_length=50)),
                ('languages', models.ManyToManyField(to='polls.language')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.person')),
            ],
        ),
    ]
