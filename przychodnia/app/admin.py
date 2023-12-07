from django.contrib import admin
from .models import *

# Register your models here.


class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'usr_imie', 'usr_nazwisko']


class KntKartyAdmin(admin.ModelAdmin):
    list_display = ['id', 'knt_nazwa', 'knt_tel', 'knt_email']


class SlownikiAdmin(admin.ModelAdmin):
    list_display = ['id', 'slw_akronim', 'slw_nazwa']


class WizystyAdmin(admin.ModelAdmin):
    list_display = ['id', 'wiz_typ', 'wiz_kntid', 'wiz_data', 'wiz_opis', 'wiz_usrid']


admin.site.register(AppUser, AppUsersAdmin)
admin.site.register(KntKarty, KntKartyAdmin)
admin.site.register(Slowniki, SlownikiAdmin)
admin.site.register(Wizyta, WizystyAdmin)


