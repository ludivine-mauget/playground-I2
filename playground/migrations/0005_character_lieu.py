# Generated by Django 2.2.28 on 2023-11-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_auto_20231109_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='lieu',
            field=models.CharField(default='Here', max_length=20),
            preserve_default=False,
        ),
    ]