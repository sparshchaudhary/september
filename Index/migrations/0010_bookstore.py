# Generated by Django 3.1.1 on 2020-09-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0009_highriskhighreturn_stockofthemonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('BookOneName', models.CharField(max_length=150)),
                ('BookOneUrl', models.URLField(max_length=500)),
                ('BookOneImage', models.ImageField(default='', upload_to='Index/images')),
                ('BookTwoName', models.CharField(max_length=150)),
                ('BookTwoUrl', models.URLField(max_length=500)),
                ('BookTwoImage', models.ImageField(default='', upload_to='Index/images')),
                ('BookThreeName', models.CharField(max_length=150)),
                ('BookThreeUrl', models.URLField(max_length=500)),
                ('BookThreeImage', models.ImageField(default='', upload_to='Index/images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
