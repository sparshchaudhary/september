# Generated by Django 3.1.1 on 2020-09-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0010_bookstore'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPic',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('NewsImage', models.ImageField(default='', upload_to='Index/images')),
            ],
        ),
    ]
