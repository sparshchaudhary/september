# Generated by Django 3.1.1 on 2020-09-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_indexnewspost'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexOtherPosts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Globalheading', models.CharField(max_length=150)),
                ('Globalcontent', models.TextField()),
                ('Globalimage', models.ImageField(default='', upload_to='Index/images')),
                ('GlobaltimeStamp', models.DateTimeField(blank=True, default=0)),
                ('Currencyheading', models.CharField(max_length=150)),
                ('Currencycontent', models.TextField()),
                ('Currencyimage', models.ImageField(default='', upload_to='Index/images')),
                ('CurrencytimeStamp', models.DateTimeField(blank=True, default=0)),
                ('Comoditiesheading', models.CharField(max_length=150)),
                ('Comoditiescontent', models.TextField()),
                ('Comoditiesimage', models.ImageField(default='', upload_to='Index/images')),
                ('ComoditiestimeStamp', models.DateTimeField(blank=True, default=0)),
                ('Otherheading', models.CharField(max_length=150)),
                ('Othercontent', models.TextField()),
                ('Otherimage', models.ImageField(default='', upload_to='Index/images')),
                ('OthertimeStamp', models.DateTimeField(blank=True, default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
