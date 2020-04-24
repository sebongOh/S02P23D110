from rest_framework import serializers
from .models import users
from .models import InputFile
from .models import cars


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'identify', 'password', 'name', 'nickname']


class InputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputFile
        fields = "__all__"


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = ['id', 'imagelink', 'name', 'price',
                  'company', 'fuel_eff', 'size', 'engine']
