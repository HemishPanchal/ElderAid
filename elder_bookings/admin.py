from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.timezone import now, timedelta
from django.db.models.functions import TruncDate
from django.db.models import Count
from elder_services.models import bookings
import json
 
class MyAdminSite(AdminSite):
    site_header = "ElderAid Admin"
 
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls
 
    def dashboard_view(self, request):
        range_type = request.GET.get('range', 'weekly')  # default is weekly
        today = now().date()
 
        if range_type == 'monthly':
            start_date = today - timedelta(days=29)
            data = (
                bookings.objects
                .filter(from_date__range=[start_date, today])
                .annotate(day=TruncDate('from_date'))
                .values('day')
                .annotate(count=Count('id'))
                .order_by('day')
            )
            labels = [entry['day'].strftime('%d %b') for entry in data]
            counts = [entry['count'] for entry in data]
        else:  # weekly
            start_date = today - timedelta(days=6)
            data = (
                bookings.objects
                .filter(from_date__range=[start_date, today])
                .annotate(day=TruncDate('from_date'))
                .values('day')
                .annotate(count=Count('id'))
                .order_by('day')
            )
            labels = [entry['day'].strftime('%a %d') for entry in data]
            counts = [entry['count'] for entry in data]
 
        context = dict(
            self.each_context(request),
            labels=json.dumps(labels),
            chart_data=json.dumps(counts),
            range=range_type,
        )
        return TemplateResponse(request, "admin/dashboard.html", context)
 
# 🔹 THIS is where admin_site is actually defined:
admin_site = MyAdminSite(name='myadmin')
