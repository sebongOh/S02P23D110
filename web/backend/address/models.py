from django.db import models

# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        # db테이블에 테이블명 명시
        db_table = 'address_address'


class Test(models.Model):
    name = models.CharField(max_length=50)
    zz = models.CharField(max_length=50)
