from rest_framework import serializers
from .models import users
from .models import InputFile


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'identify', 'password', 'name', 'nickname']


class InputFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputFile
        fields = "__all__"
