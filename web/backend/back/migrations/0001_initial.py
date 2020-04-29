# Generated by Django 3.0.5 on 2020-04-28 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagelink', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=60)),
                ('company', models.CharField(max_length=50)),
                ('fuel_eff', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('engine', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'back_cars',
            },
        ),
        migrations.CreateModel(
            name='InputFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identify', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'back_users',
            },
        ),
        migrations.CreateModel(
            name='likecar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.users')),
            ],
        ),
        migrations.CreateModel(
            name='carlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.users')),
            ],
        ),
    ]
