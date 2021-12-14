from django.urls import path 
from .import views 

app_name = 'tk_users'

urlpatterns = [
    # ex: /tk_users/
    path('',views.index, name="index"),
    
    path('general_user/', views.general_user, name="general_user"),
    path('admin_user/', views.admin_user, name="admin_user"),
    path('admin_cognito_user_list/', views.admin_cognito_user_list, name="admin_cognito_user_list"),
    #path('<int:use>',views.show,name='show')  # HTML LINK FOR THIS <a href="{% url 'tk_users:show' cognito_user.user_id %}">
]