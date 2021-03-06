# Generated by Django 3.0.6 on 2020-07-14 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='maplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapName', models.CharField(max_length=60)),
                ('mapDesc', models.TextField()),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('mapTel', models.CharField(max_length=20)),
                ('mapAddr', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='maplist1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapName', models.CharField(max_length=60)),
                ('mapDesc', models.TextField()),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('mapTel', models.CharField(max_length=20)),
                ('mapAddr', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='maplist2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapName', models.CharField(max_length=60)),
                ('mapDesc', models.TextField()),
                ('mapLat', models.CharField(max_length=20)),
                ('mapLng', models.CharField(max_length=20)),
                ('mapTel', models.CharField(max_length=20)),
                ('mapAddr', models.CharField(max_length=60)),
            ],
        ),
    ]
