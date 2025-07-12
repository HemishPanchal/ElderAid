from django.contrib import admin
from .models import user_info, services, sub_services, bookings

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_name', 'service_id']

class SubServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'subservice_name', 'service_id', 'price']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'service_id', 'subservice_id', 'booking_time','price','from_date','to_date']

admin.site.register(user_info)
admin.site.register(services, ServiceAdmin)
admin.site.register(sub_services, SubServiceAdmin)
admin.site.register(bookings, BookingAdmin)
