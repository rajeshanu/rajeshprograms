# Generated by Django 2.1.1 on 2018-10-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.IntegerField(default=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quntity', models.IntegerField(default=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
