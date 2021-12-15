from django.urls import path 
from .import views 

app_name = 'tk_users'

urlpatterns = [
    # ex: /tk_users/
    path('',views.index, name="index"),
    
    path('general_user/', views.general_user, name="general_user"),
    path('admin_user/', views.admin_user, name="admin_user"),
    path('admin_cognito_user_list/', views.admin_cognito_user_list, name="admin_cognito_user_list"),
    path('admin_cognito_user_add/', views.admin_cognito_user_add, name="admin_cognito_user_add"),
    #path('admin_cl/', views.admin_cognito_user_adding, name="admin_cognito_user_adding"),
]