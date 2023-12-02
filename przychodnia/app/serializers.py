from rest_framework import serializers, validators, generics
from .models import *


class KntSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    knt_create_date = serializers.DateTimeField(read_only=True)
    knt_lastmod_date = serializers.DateTimeField(read_only=True)

    knt_nazwa = serializers.CharField(required=True)
    knt_tel = serializers.CharField(required=True)


class WizytaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    wiz_usrid = serializers.IntegerField(read_only=True)

class Meta:
    model = AppUser
    fields = ['id','usr_imie','usr_nazwisko']

class AppUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    usr_imie = serializers.CharField(required=True)
    usr_nazwisko = serializers.CharField(required=True)


class Meta:
    model = AppUser
    fields = ['id','usr_imie','usr_nazwisko']