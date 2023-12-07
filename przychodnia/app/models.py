import datetime

from django.db import models
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
# Create your models here.


class Slowniki(models.Model):
    slw_akronim = models.CharField(max_length=5, null=False)
    slw_nazwa = models.CharField(max_length=50, null=False)


class AppUser(models.Model):
    usr_imie = models.CharField(max_length=30, null=False)
    usr_nazwisko = models.CharField(max_length=30, null=False)


class KntKarty(models.Model):

    def __str__(self):
        return f'{self.knt_nazwa}'

    knt_nazwa = models.CharField(max_length=50, null=False, unique=True)
    knt_tel = models.CharField(max_length=12, null=False)
    knt_email = models.CharField(max_length=40, null=True, unique=True)
    knt_create_userid = models.ForeignKey(AppUser, null=True, on_delete=models.SET_NULL)
    knt_create_date = models.DateTimeField(default=datetime.datetime.now())
    knt_lastmod_date = models.DateTimeField(default=datetime.datetime.now())


class Wizyta(models.Model):
    wiz_typ = models.ForeignKey(Slowniki, null=True, on_delete=models.SET_NULL)
    wiz_data = models.DateTimeField()
    wiz_kntid = models.ForeignKey(KntKarty, null=True, on_delete=models.SET_NULL)
    wiz_usrid = models.ForeignKey(AppUser, null=True, on_delete=models.SET_NULL)
    wiz_opis = models.CharField(max_length=255)
