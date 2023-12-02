from django.contrib import admin
from .models import *

# Register your models here.


class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'usr_imie', 'usr_nazwisko']


class KntKartyAdmin(admin.ModelAdmin):
    list_display = ['id', 'knt_nazwa', 'knt_tel', 'knt_email']


admin.site.register(AppUser, AppUsersAdmin)
admin.site.register(KntKarty, KntKartyAdmin)


