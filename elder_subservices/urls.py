from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.subservices_add,name='subservices_insert'),
    path('<int:id>/', views.subservices_add,name='subservices_update'),
    path('delete/<int:id>/', views.subservices_delete,name='subservices_delete'),
    path('list/',views.subservices_list,name='subservices_list'),
]