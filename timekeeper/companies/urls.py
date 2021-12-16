from django.urls import path 
from .import views 

app_name = 'companies'

urlpatterns = [
    # pages
    #path('',views.index, name="index"),
    path('admin_company_list/', views.admin_company_list, name="admin_company_list"),
    path('admin_company_add/', views.admin_company_add, name="admin_company_add"),
    path('admin_company_add_error/', views.admin_company_add_error, name="admin_company_add_error"),
    #path('adminUser', views.adminUser, name="adminUser"),
    #path('generalUser', views.generalUser, name="generalUser"),
]