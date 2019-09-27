# Generated by Django 2.2.5 on 2019-09-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=25)),
                ('nameofcity', models.CharField(max_length=25)),
                ('weather_name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=200)),
                ('icon', models.TextField(max_length=200)),
            ],
        ),
    ]