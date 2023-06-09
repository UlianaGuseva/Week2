# Generated by Django 4.2 on 2023-05-03 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('rent', '0006_customer_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userprofile')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.vehicle')),
            ],
        ),
    ]
