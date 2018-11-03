# Generated by Django 2.1.1 on 2018-10-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('desig', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
