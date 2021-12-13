from django.urls import path 
from .import views 

app_name = 'companies'

urlpatterns = [
    # pages
    path('',views.index, name="index"),
    path('adminUser', views.adminUser, name="adminUser"),
    path('generalUser', views.generalUser, name="generalUser"),
]