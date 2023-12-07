from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('adduser/', views.usr_insert),
    path('visits/', views.wizyty_list),
    path('addknt/', views.knt_insert),
    path('api-auth/', include('rest_framework.urls')),
]