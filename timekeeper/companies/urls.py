from django.urls import path 
from .import views 

#from django.conf.urls import url

app_name = 'companies'

urlpatterns = [
    # pages
    path('admin_company_list/', views.admin_company_list, name="admin_company_list"),
    #path(r'^admin_company_list_paginated/(?P<page>[0-9]+)/$', views.admin_company_list_paginated, name="admin_company_list_paginated"),
    #path('admin_company_list_paginated/<int>/', views.admin_company_list_paginated, name="admin_company_list_paginated"),
    #path(r'admin_company_list_paginated/(?P<page>\d+)/$', views.admin_company_list_paginated, name="admin_company_list_paginated"),
   
    path('admin_company_add/', views.admin_company_add, name="admin_company_add"),
    path('admin_company_add_error/', views.admin_company_add_error, name="admin_company_add_error"),

]