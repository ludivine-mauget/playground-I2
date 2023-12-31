# Generated by Django 2.2.28 on 2023-11-13 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0009_auto_20231112_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id_lieu', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('disponibilite', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.Lieu'),
        ),
    ]
