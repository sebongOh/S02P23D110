# Generated by Django 3.0.5 on 2020-04-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='likecars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carId', models.IntegerField()),
                ('userId', models.IntegerField()),
            ],
            options={
                'db_table': 'back_likecars',
            },
        ),
    ]
