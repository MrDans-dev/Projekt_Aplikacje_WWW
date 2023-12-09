from rest_framework import serializers, validators, generics
from .models import *


class SlownikSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slw_akronim = serializers.CharField(required=True)
    slw_nazwa = serializers.CharField(required=True)

    def create(self, validated_data):
        return Slowniki.objects.create(**validated_data)

    class Meta:
        model = Slowniki
        fields = '__all__'


class KntSerializer(serializers.ModelSerializer):
    class Meta:
        model = KntKarty
        fields = '__all__'
    id = serializers.IntegerField(read_only=True)
    knt_nazwa = serializers.CharField(required=True)
    knt_tel = serializers.CharField(required=True)
    knt_email = serializers.CharField()

    def create(self, validated_data):
        return KntKarty.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.knt_nazwa = validated_data.get('knt_nazwa', instance.knt_nazwa)
        instance.knt_tel = validated_data.get('knt_tel', instance.knt_tel)
        instance.knt_email = validated_data.get('knt_email', instance.knt_email)
        create_userid_data = validated_data.get('knt_create_userid')
        if create_userid_data:
            instance.knt_create_userid = create_userid_data
        instance.knt_lastmod_date = datetime.datetime.now()
        instance.save()
        return instance


class AppUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    usr_imie = serializers.CharField(required=True)
    usr_nazwisko = serializers.CharField(required=True)

    def create(self, validated_data):
        return AppUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.usr_imie = validated_data.get('usr_imie', instance.usr_imie)
        instance.usr_nazwisko = validated_data.get('usr_nazwisko', instance.usr_nazwisko)
        instance.save()
        return instance

    class Meta:
        model = AppUser
        fields = ['id', 'usr_imie', 'usr_nazwisko']


class WizytaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    wiz_data = serializers.DateTimeField()
    knt = KntSerializer(many=False,source='wiz_kntid')
    rodzaj_wiz = SlownikSerializer(many=False,source='wiz_typ')
    wiz_add_user = AppUserSerializer(many=False, source='wiz_usrid')

    def create(self, validated_data):
        slownik_data = validated_data.pop('wiz_typ', Slowniki)
        knt_data = validated_data.pop('knt', KntKarty)
        app_user_data = validated_data.pop('wiz_usrid', AppUser)

    def to_internal_value(self, data):
        rodzaj_wiz_data = data.get('wiz_typ')
        if rodzaj_wiz_data and isinstance(rodzaj_wiz_data, dict):
            slownik_serializer = SlownikSerializer(data=rodzaj_wiz_data)
            slownik_serializer.is_valid(raise_exception=True)
            return {'wiz_typ': slownik_serializer.save()}
        return super().to_internal_value(data)

    class Meta:
        model = Wizyta
        fields = ['id', 'wiz_data', 'knt', 'wiz_add_user', 'wiz_opis', 'rodzaj_wiz']



