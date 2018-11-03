# Generated by Django 2.1.1 on 2018-10-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(default=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cno', models.IntegerField(default=2)),
            ],
        ),
    ]