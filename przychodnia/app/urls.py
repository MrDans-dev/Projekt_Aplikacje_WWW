from django.urls import path, include
from . import views

urlpatterns = [
    #GET
    path('users/', views.user_list),
    path('knt/', views.knt_list),
    path('knthistory/', views.knthistory),
    path('visits/', views.wizyty_list),
    path('slw/', views.slowniki_list),
    path('wiz_tocall', views.wizyty_to_call),


    #INSERT
    path('adduser/', views.usr_insert),
    path('addvisit/', views.wizyta_insert),
    path('addknt/', views.knt_insert),
    path('addslw/', views.slw_insert),

    #UPDATE DELETE
    path('knt_update_delete/<int:pk>/', views.knt_update_delete),
    path('visit_update_delete/<int:pk>/', views.wizyta_update_delete),
    path('slw_update_delete/<int:pk>/', views.slowniki_update_delete),
    path('user_update_delete/<int:pk>/', views.user_update_delete),

    path('api-auth/', include('rest_framework.urls')),
]