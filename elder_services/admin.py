from django.contrib import admin
from .models import user_info, services, sub_services, bookings
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from admincharts.admin import AdminChartMixin
from django.db.models import Sum
from elder_bookings.admin import admin_site


def booking_table(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['user_id', 'service_id', 'subservice_id','booking_time','price','from_date','to_date']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.user_id, obj.service_id, obj.subservice_id,obj.booking_time,obj.price,obj.from_date,obj.to_date])
   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

booking_table.short_description = "Export to PDF"

class BookingAdmin(admin.ModelAdmin):
    list_display  = [
        'id', 'user_id', 'service_id', 'subservice_id',
        'booking_time', 'price', 'from_date', 'to_date',
    ]
    search_fields = ['user_id__uname']
    actions       = [booking_table]          # you already added this




class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_name', 'service_id']
    search_fields = ['service_name',]

class SubServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'subservice_name', 'service_id', 'price']
    search_fields = ['subservice_name',]


admin.site.register(user_info)
admin.site.register(services, ServiceAdmin)
admin.site.register(sub_services, SubServiceAdmin)
admin.site.register(bookings, BookingAdmin)

admin_site.register(user_info)
admin_site.register(services, ServiceAdmin)
admin_site.register(sub_services, SubServiceAdmin)
admin_site.register(bookings, BookingAdmin)
 
 