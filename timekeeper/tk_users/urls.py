from django.urls import path 
from .import views 

app_name = 'tk_users'

urlpatterns = [
    # pages
    path('',views.index, name="index"),
    path('general_user/', views.general_user, name="general_user"),
    path('admin_user/', views.admin_user, name="admin_user"),
    path('admin_cognito_users/', views.admin_cognito_users, name="admin_cognito_users"),
]