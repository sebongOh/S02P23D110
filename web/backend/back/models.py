from django.db import models
import bz2
# Create your models here.


class users(models.Model):
    id = models.AutoField(primary_key=True)
    identify = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    nickname = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'back_users'


class InputFile(models.Model):

    file = models.FileField(blank=False, null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.file.name


class cars(models.Model):
    id = models.AutoField(primary_key=True)
    imagelink = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    company = models.CharField(max_length=50)
    fuel_eff = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)

    class Meta:
        db_table = 'back_cars'


class preference(models.Model):
    id = models.AutoField(primary_key=True)
