# Generated by Django 3.1.1 on 2020-09-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0011_newspic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspic',
            old_name='NewsImage',
            new_name='NewsImage1',
        ),
        migrations.AddField(
            model_name='newspic',
            name='NewsImage2',
            field=models.ImageField(default='', upload_to='Index/images'),
        ),
        migrations.AddField(
            model_name='newspic',
            name='NewsImage3',
            field=models.ImageField(default='', upload_to='Index/images'),
        ),
    ]
