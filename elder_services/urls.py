from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.services_add,name='services_insert'),
    path('<int:id>/', views.services_add,name='services_update'),
    path('delete/<int:id>/', views.services_delete,name='services_delete'),
    path('list/',views.services_list,name='services_list'),
]