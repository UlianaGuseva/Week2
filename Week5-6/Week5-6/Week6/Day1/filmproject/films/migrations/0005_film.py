# Generated by Django 4.2 on 2023-05-02 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('release_date', models.DateField(auto_now_add=True)),
                ('available_in_countries', models.ManyToManyField(related_name='film_available', to='films.country')),
                ('category', models.ManyToManyField(to='films.category')),
                ('created_in_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='film_created', to='films.country')),
                ('director', models.ManyToManyField(to='films.director')),
            ],
        ),
    ]
