# Generated by Django 2.1.1 on 2018-10-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('sno', models.IntegerField(default=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(default=10)),
                ('path', models.CharField(max_length=80)),
            ],
        ),
    ]
