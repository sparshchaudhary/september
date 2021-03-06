# Generated by Django 3.1.1 on 2020-09-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0008_stockoftheweek'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighRiskHighReturn',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('sector', models.CharField(max_length=20)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='Index/images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='StockOfTheMonth',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('sector', models.CharField(max_length=20)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='Index/images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
