# Generated by Django 3.1.1 on 2020-09-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0003_stockcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcard',
            name='id',
            field=models.CharField(default=' ', max_length=150),
            preserve_default=False,
        ),
    ]