# Generated by Django 4.1.7 on 2023-03-25 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodAllergies_App', '0002_delete_foodallergy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='allergy',
            field=models.ForeignKey(default='blank', on_delete=django.db.models.deletion.CASCADE, to='foodAllergies_App.allergy'),
        ),
        migrations.AlterField(
            model_name='category',
            name='food',
            field=models.ManyToManyField(default='blank', to='foodAllergies_App.food'),
        ),
    ]
