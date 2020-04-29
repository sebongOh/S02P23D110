from rest_framework import serializers
from .models import users
from .models import InputFile
from .models import cars
from .models import likecar
from .models import carlike


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'identify', 'password', 'name', 'nickname', 'image']


class InputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputFile
        fields = "__all__"


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = ['id', 'imagelink', 'name', 'price',
                  'company', 'fuel_eff', 'size', 'engine']


class LikecarSerializer(serializers.ModelSerializer):
    class Meta:
        model = likecar
        fields = ['id', 'user', 'car']


class carLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = carlike
        fields = ['user', 'car']
