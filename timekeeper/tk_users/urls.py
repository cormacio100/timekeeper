from django.contrib import admin
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .import views 

app_name = 'tk_users'

urlpatterns = [
    # ex: /tk_users/
    path('',views.index, name="index"),
    
    path('general_user/', views.general_user, name="general_user"),
    path('general_user_upload_expenses/', views.general_user_upload_expenses, name="general_user_upload_expenses"),
    path('admin_user/', views.admin_user, name="admin_user"),
    path('admin_cognito_user_list/', views.admin_cognito_user_list, name="admin_cognito_user_list"),
    path('admin_cognito_user_add/', views.admin_cognito_user_add, name="admin_cognito_user_add"),
    #path('admin_cognito_user_error/', views.admin_cognito_user_error, name="admin_cognito_user_error"),
    #path('admin_cl/', views.admin_cognito_user_adding, name="admin_cognito_user_adding"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)