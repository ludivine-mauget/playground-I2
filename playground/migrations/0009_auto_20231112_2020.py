# Generated by Django 2.2.28 on 2023-11-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_auto_20231111_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='disponibilite',
            field=models.CharField(max_length=20),
        ),
    ]