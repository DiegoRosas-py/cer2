# Generated by Django 5.0.6 on 2024-07-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_pokemon_image_pokemon_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(default='No existe descripcion para este pokemon', max_length=200),
        ),
    ]
