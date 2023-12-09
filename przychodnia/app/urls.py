from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('knt/', views.knt_list),
    path('visit/<int:pk>/', views.wizyta),
    path('visits/', views.wizyty_list),
    path('adduser/', views.usr_insert),
    path('addvisit/', views.wizyta_insert),
    path('addknt/', views.knt_insert),
    path('knt_update_delete/<int:pk>/', views.knt_update_delete),
    path('api-auth/', include('rest_framework.urls')),
]