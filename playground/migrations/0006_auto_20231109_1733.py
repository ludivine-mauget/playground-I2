# Generated by Django 2.2.28 on 2023-11-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_character_lieu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='photo',
            field=models.ImageField(upload_to='media', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='photo',
            field=models.ImageField(upload_to='media', verbose_name=''),
        ),
    ]
