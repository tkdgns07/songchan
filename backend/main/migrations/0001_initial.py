# Generated by Django 5.1 on 2024-09-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calendar_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('student', models.CharField(default='None', max_length=10)),
                ('music_url', models.CharField(default='None', max_length=150)),
            ],
        ),
    ]
