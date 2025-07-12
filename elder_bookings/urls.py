from django.urls import path, include
from . import views

urlpatterns=[
    path('bookservice/', views.book_service, name='get_service'),
    path('bookservice/<int:id>/booksubservice/', views.book_subservice, name='get_subservice'),
    path('confirm/<int:id>/',views.booking_confirm,name='booking_confirm'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]