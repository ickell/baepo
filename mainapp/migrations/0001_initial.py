# Generated by Django 2.2.3 on 2019-08-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('survived', models.BooleanField()),
                ('age', models.FloatField()),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(max_length=100)),
            ],
        ),
    ]
