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


class test(models.Model):
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)


class InputFile(models.Model):

    file = models.FileField(blank=False, null=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.file.name


class InputImage(models.Model):

    imagename = models.CharField(max_length=30)
    image = models.ImageField(default='media/test.jpg')
