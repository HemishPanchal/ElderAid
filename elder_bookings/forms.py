from django import forms
from elder_services.models import bookings
from django.utils import timezone
class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = ['booking_time', 'from_date', 'to_date']
        widgets = {
            'booking_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'value': timezone.now().strftime('%Y-%m-%dT%H:%M'),
            }),
            'from_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'to_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }